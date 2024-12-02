# IsInPlayerEnemyFaction
def is_in_player_enemy_faction(character):
    faction = character.GetFaction()
    if faction == 2 or faction == 3 or faction == 4 or faction == 16:
        return 1
    return 0

# IsGameStateCombat
def is_game_state_combat():
    game_state = GetGameState()
    if game_state == 3:
        return 1
    return 0

# IsPlayerInsideCamp
def is_player_inside_camp(game):
    value = game.GetBlackboardValueFromObject(0x72CD5541)  # Assuming the byte pattern is a constant reference
    if value is None:
        return 0
    if value > 0:
        return 1
    return 0

# IsGameStateRelaxed
def is_game_state_relaxed():
    game_state = GetGameState()
    if game_state == 1:
        return 1
    return 0

# IsGameModeInVehicle
def is_game_mode_in_vehicle():
    game_mode = GetGameMode()
    if game_mode == 2:
        return 1
    return 0

# GetMaximumParryAmount
def get_maximum_parry_amount(character):
    upgrade_level = character.GetUpgradeLevel("weapon_parry")
    if upgrade_level > 0:
        return 2
    wielded_object = character.GetWieldedObject()
    if wielded_object is None:
        return 2
    if wielded_object.IsItemCategory("Knife"):
        return 2
    if wielded_object.IsItemCategory("Club") or wielded_object.IsItemCategory("ThunderStick") or wielded_object.IsItemCategory("Spear"):
        return 2
    return 0

# METERS_FOR_OGC_ENEMIES_NEAR_TO_TRIGGER_COMBAT
def meters_for_ogc_enemies_near_to_trigger_combat():
    return 15

# IsGameModeOnGround
def is_game_mode_on_ground():
    game_mode = GetGameMode()
    if game_mode == 1:
        return 1
    return 0

# GetGameMode
def get_game_mode(game):
    return game.GetBlackboardValueFromObject(0x13, 0x3C6C8C)

# ENEMY_VEHICLE_RADIUS
def enemy_vehicle_radius():
    return 100

# GetGameState
def get_game_state(game):
    return game.GetBlackboardValueFromObject(0x95F3A074)

# IsGameStateAlerted
def is_game_state_alerted():
    game_state = GetGameState()
    if game_state == 2:
        return 1
    return 0
