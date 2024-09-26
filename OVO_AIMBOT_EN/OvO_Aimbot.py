import os

cfg_file_path = 'ovo_aimbot.cfg'
nut_file_path = 'vpk_editor/englishclient_mp_common.bsp.pak000_dir/scripts/vscripts/_utility_shared.nut'
pilot_base_set_path = 'vpk_editor/englishclient_mp_common.bsp.pak000_dir/scripts/players/mp/pilot_base.set'
pilot_base_txt_path = 'vpk_editor/englishclient_mp_common.bsp.pak000_dir/scripts/players/mp/pilot_base.txt'
engine_materials_path = 'vpk_editor/englishclient_mp_common.bsp.pak000_dir/materials/engine/cloak.vmt'

# Read the contents of the cfg file
with open(cfg_file_path, 'r', encoding='utf-8') as cfg_file:
    cfg_lines = cfg_file.readlines()

# Create a dictionary to store variables from the cfg and their entire line contents
cfg_dict = {}
player_fov_value = None
draw_clock_value = None
for line in cfg_lines:
    if line.strip() and not line.strip().startswith('//') and 'misc' not in line:
        key = line.split('=')[0].strip()
        cfg_dict[key] = line.strip()  # Retain the entire line
        if key == 'player_fov':
            player_fov_value = line.split('=')[1].strip().split(';')[0]  # Extract fov value
        elif key == 'draw_clock':
            draw_clock_value = line.split('=')[1].strip().split(';')[0]  # Extract draw_clock value

# Update the nut file
with open(nut_file_path, 'r', encoding='utf-8') as nut_file:
    nut_lines = nut_file.readlines()

for i, nut_line in enumerate(nut_lines):
    for key in cfg_dict.keys():
        if f"{key} =" in nut_line:
            nut_lines[i] = cfg_dict[key] + '\n'  # Replace with the entire line from cfg

with open(nut_file_path, 'w', encoding='utf-8') as nut_file:
    nut_file.writelines(nut_lines)

# Update pilot_base.set and pilot_base.txt files
for file_path in [pilot_base_set_path, pilot_base_txt_path]:
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if 'fov' in line or 'viewmodelfov' in line:
            # Replace with player_fov_value, retaining the original format
            line_parts = line.split()  # Split by space
            new_line = line.rstrip()  # Remove line ending
            last_space_index = new_line.rfind(' ')
            new_line = new_line[:last_space_index + 1] + player_fov_value  # Replace value
            lines[i] = new_line + '\n'  # Add newline

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

# Update the engine materials file
with open(engine_materials_path, 'r', encoding='utf-8') as file:
    engine_lines = file.readlines()

# Determine the replacement value
new_write_color_value = '"1"' if draw_clock_value.lower() == 'true' else '"0"'

for i, line in enumerate(engine_lines):
    if '"$writeColor"' in line:
        # Replace "$writeColor" value, retaining the original spacing
        space_index = line.find('"$writeColor"') + len('"$writeColor"')
        line = line[:space_index] + f' {new_write_color_value}\n'  # Replace value
        engine_lines[i] = line

with open(engine_materials_path, 'w', encoding='utf-8') as file:
    file.writelines(engine_lines)

print("Update complete!")
