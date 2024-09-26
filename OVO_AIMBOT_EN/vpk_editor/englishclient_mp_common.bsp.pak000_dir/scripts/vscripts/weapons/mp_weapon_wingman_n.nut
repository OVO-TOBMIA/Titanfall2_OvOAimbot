global function MpWeaponWINGMAN_N_Init()

function MpWeaponWINGMAN_N_Init()
{
	SmartAmmo_SetAllowUnlockedFiring( weapon, true )
	SmartAmmo_SetUnlockAfterBurst( weapon, (SMART_AMMO_PLAYER_MAX_LOCKS > 5) )
	SmartAmmo_SetWarningIndicatorDelay( weapon, 0.0 )
}