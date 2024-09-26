import os

cfg_file_path = 'ovo_aimbot.cfg'
nut_file_path = 'vpk_editor/englishclient_mp_common.bsp.pak000_dir/scripts/vscripts/_utility_shared.nut'
pilot_base_set_path = 'vpk_editor/englishclient_mp_common.bsp.pak000_dir/scripts/players/mp/pilot_base.set'
pilot_base_txt_path = 'vpk_editor/englishclient_mp_common.bsp.pak000_dir/scripts/players/mp/pilot_base.txt'
engine_materials_path = 'vpk_editor/englishclient_mp_common.bsp.pak000_dir/materials/engine/cloak.vmt'

# 读取cfg文件内容
with open(cfg_file_path, 'r', encoding='utf-8') as cfg_file:
    cfg_lines = cfg_file.readlines()

# 创建一个字典来存储cfg中的变量及其整行内容
cfg_dict = {}
player_fov_value = None
draw_clock_value = None
for line in cfg_lines:
    if line.strip() and not line.strip().startswith('//') and 'misc' not in line:
        key = line.split('=')[0].strip()
        cfg_dict[key] = line.strip()  # 保留整行内容
        if key == 'player_fov':
            player_fov_value = line.split('=')[1].strip().split(';')[0]  # 提取fov值
        elif key == 'draw_clock':
            draw_clock_value = line.split('=')[1].strip().split(';')[0]  # 提取draw_clock值

# 更新nut文件
with open(nut_file_path, 'r', encoding='utf-8') as nut_file:
    nut_lines = nut_file.readlines()

for i, nut_line in enumerate(nut_lines):
    for key in cfg_dict.keys():
        if f"{key} =" in nut_line:
            nut_lines[i] = cfg_dict[key] + '\n'  # 替换为cfg中的整行

with open(nut_file_path, 'w', encoding='utf-8') as nut_file:
    nut_file.writelines(nut_lines)

# 更新pilot_base.set和pilot_base.txt文件
for file_path in [pilot_base_set_path, pilot_base_txt_path]:
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if 'fov' in line or 'viewmodelfov' in line:
            # 替换为player_fov_value，保留原行的格式
            line_parts = line.split()  # 按空格分割
            new_line = line.rstrip()  # 去除行尾换行符
            last_space_index = new_line.rfind(' ')
            new_line = new_line[:last_space_index + 1] + player_fov_value  # 替换值
            lines[i] = new_line + '\n'  # 添加换行符

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

# 更新engine材料文件
with open(engine_materials_path, 'r', encoding='utf-8') as file:
    engine_lines = file.readlines()

# 确定替换值
new_write_color_value = '"1"' if draw_clock_value.lower() == 'true' else '"0"'

for i, line in enumerate(engine_lines):
    if '"$writeColor"' in line:
        # 替换"$writeColor"的值，保留原行的空格格式
        space_index = line.find('"$writeColor"') + len('"$writeColor"')
        line = line[:space_index] + f' {new_write_color_value}\n'  # 替换值
        engine_lines[i] = line

with open(engine_materials_path, 'w', encoding='utf-8') as file:
    file.writelines(engine_lines)

print("更新完成！")
