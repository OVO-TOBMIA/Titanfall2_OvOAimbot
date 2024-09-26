global function MpWeaponR97_Init()

function MpWeaponR97_Init()
{
	SmartAmmo_SetAllowUnlockedFiring( weapon, true )
	SmartAmmo_SetUnlockAfterBurst( weapon, (SMART_AMMO_PLAYER_MAX_LOCKS > 5) )
	SmartAmmo_SetWarningIndicatorDelay( weapon, 0.0 )
}