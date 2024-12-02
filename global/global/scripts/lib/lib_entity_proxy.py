def get_explosion_handler(obj):
    explosion_handler = SafeGetChildByScriptName(obj, "explosion_damage_handler.xpy")
    return explosion_handler

def get_vehicle_gameplay(obj):
    vehicle_gameplay = SafeGetChild(obj, "script.gameplay")
    return vehicle_gameplay

def get_aero(obj):
    aero = SafeGetChildByScriptName(obj, "vpaerodynamics.xpy")
    return aero

def get_vehicle_stats(obj):
    vehicle_stats = SafeGetChild(obj, "script.vehicle.stats")
    return vehicle_stats

def get_player_weapon_handling():
    player_weapon_handling = game.GetGameObjectByAlias("script.player.weapon.handling")
    return player_weapon_handling

def get_sider_burner(obj):
    sider_burner = SafeGetChild(obj, "script.weapon.sideburner")
    return sider_burner

def get_harpoon(obj):
    harpoon = SafeGetChild(obj, "script.weapon.harpoon")
    return harpoon

def get_shotgun_target(obj):
    shotgun_target = SafeGetChild(obj, "script.shotgun_target.base")
    return shotgun_target

def get_damage_tracker(obj):
    damage_tracker = SafeGetChild(obj, "script.damagesystem.DamageTracker")
    return damage_tracker

def get_chumbucket():
    chumbucket = game.GetGameObjectByAlias("chumbucket")
    return chumbucket

def get_signature_vehicle_gameplay_script():
    signature_vehicle = vehicle.GetSignatureVehicle()
    signature_vehicle_gameplay = SafeGetChild(signature_vehicle, "script.gameplay")
    return signature_vehicle_gameplay

def safe_get_child_by_script_name(obj, script_name):
    if obj is None:
        debug.LogError("SafeGetChildByScriptName() called with object=None")
        return None
    child = game.GetChildByScriptName(obj, script_name)
    if child is None:
        debug.LogError(f"missing script subobject using {script_name}")
    return child

def safe_get_child(obj, script_name):
    if obj is None:
        debug.LogError("SafeGetChild() called with object=None")
        return None
    child = game.GetChild(obj, script_name)
    return child

def get_body_health(obj):
    weakspot = GetBodyWeakspot(obj)
    body_health = game.WeakspotGetHealthScript(weakspot)
    return body_health

def get_weakspot_list(obj):
    weakspot_list = game.GetChild(obj, "Weakspots")
    return weakspot_list

def get_player_input(obj):
    player_input = SafeGetChildByScriptName(obj, "veh_player_input.xpy")
    return player_input

def get_fire_damage_handler(obj):
    fire_damage_handler = SafeGetChildByScriptName(obj, "fire_damage_handler.xpy")
    return fire_damage_handler

def get_weakspot_human(obj):
    weakspot_human = game.GetChildWithNameHash(obj, bytes([73, 93, 184, 255]))
    return weakspot_human

def get_tension_damage(obj):
    tension_damage_handler = SafeGetChild(obj, "script.damagesystem.TensionDamageHandler")
    return tension_damage_handler

def get_shotgun(obj):
    shotgun = SafeGetChild(obj, "script.weapon.shotgun")
    return shotgun

def get_player_data(obj):
    player_data = SafeGetChildByScriptName(obj, "veh_player_data.xpy")
    return player_data

def get_shotgun_anim_loader(obj):
    shotgun_anim_loader = SafeGetChildByScriptName(obj, "veh_shotgun_anim_loader.xpy")
    return shotgun_anim_loader

def get_global_shotgun_target_list():
    shotgun_target_list = game.GetGameObjectByAlias("shotgun_target_list")
    return shotgun_target_list

def get_repair(obj):
    body_health = GetBodyHealth(obj)
    repair = SafeGetChild(body_health, "script.damagesystem.StoppedState")
    return repair

def get_collision(obj):
    collision_damage_handler = SafeGetChildByScriptName(obj, "collision_damage_handler.xpy")
    return collision_damage_handler

def get_grill_weakspot(obj):
    weakspots = SafeGetChild(obj, "Weakspots")
    grill_weakspot = SafeGetChild(weakspots, "VehicleWeakspot.Grill")
    return grill_weakspot

def get_global_harpoon_target_list():
    harpoon_target_list = game.GetGameObjectByAlias("harpoon_target_list")
    return harpoon_target_list

def get_flamethrower(obj):
    flamethrower = SafeGetChild(obj, "script.weapon.flamethrower")
    return flamethrower

def get_harpoon_data_weapon(obj):
    harpoon_data = None
    harpoon = game.GetChildWithNameHash(obj, bytes([246, 213, 201, 74]))
    if harpoon:
        harpoon_data = game.GetChildWithNameHash(harpoon, bytes([198, 161, 241, 254]))
    return harpoon_data

def get_chum_gameplay(obj):
    chum_gameplay = SafeGetChild(obj, "ScriptGameplay")
    return chum_gameplay

def get_sniper(obj):
    sniper = SafeGetChild(obj, "script.weapon.sniper")
    return sniper

def get_body_weakspot(obj):
    weakspots = SafeGetChild(obj, "Weakspots")
    body_weakspot = SafeGetChild(weakspots, "VehicleWeakspot.Body")
    return body_weakspot

def get_boost(obj):
    boost = SafeGetChild(obj, "script.boost")
    return boost

def get_health_id(obj):
    health_id = SafeGetChild(obj, "script.damagesystem.HealthId")
    return health_id
