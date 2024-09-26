global function MpWeaponCAR_Init()

// 初始化函数
function MpWeaponCAR_Init()
{
    SmartAmmo_SetAllowUnlockedFiring(weapon, true);
    SmartAmmo_SetUnlockAfterBurst(weapon, (SMART_AMMO_PLAYER_MAX_LOCKS > 5));
    SmartAmmo_SetWarningIndicatorDelay(weapon, 0.0);

}