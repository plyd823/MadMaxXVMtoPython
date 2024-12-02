# Assumed utility functions for global access, property getting, and event handling
def log_info(message):
    print(message)

def send_event(event_name, data=""):
    print(f"Sending event: {event_name} with data: {data}")

def register_event_handler(handler_name, function):
    print(f"Registering event handler: {handler_name} -> {function.__name__}")

def get_global_properties():
    # Simulating getting vehicle global properties
    return {
        "BoardingSwayDebugEnabled": False,
        "BoardingShakeOffEnabled": False,
        "BoardingLandDebugEnabled": False,
        "print_vehicle_collision_effect_positions": False,
        "showIsDeformingDebug": False,
        "showHealthbarDebug": False,
        "print_dmgtracker_debug": False,
        "print_nondmg_debug": False,
        "showTireSizeDebug": False,
        "showGgDebug": False
    }

def set_vehicle_property(property_name, value):
    print(f"Setting vehicle property {property_name} = {value}")


# BoardingEnableSwayDebug function
def boarding_enable_sway_debug():
    log_info("Vehicle Debug Menu, BoardingEnableSwayDebug")
    vehicle_properties = get_global_properties()
    vehicle_properties['BoardingSwayDebugEnabled'] = True
    set_vehicle_property("BoardingSwayDebugEnabled", True)

# ToggleDeformDebug function
def toggle_deform_debug():
    vehicle_properties = get_global_properties()
    vehicle_properties['showIsDeformingDebug'] = not vehicle_properties['showIsDeformingDebug']
    set_vehicle_property("showIsDeformingDebug", vehicle_properties['showIsDeformingDebug'])
    if vehicle_properties['showIsDeformingDebug']:
        log_info("IsDeforming Display activated")
        send_event("vehicle.debugscript.render.start")
    else:
        log_info("IsDeforming Display deactivated")

# BoardingEnableLandDebug function
def boarding_enable_land_debug():
    log_info("Vehicle Debug Menu, BoardingEnableLandDebug")
    vehicle_properties = get_global_properties()
    vehicle_properties['BoardingLandDebugEnabled'] = True
    set_vehicle_property("BoardingLandDebugEnabled", True)

# ToggleVehicleCollisionEffectPositionsDebug function
def toggle_vehicle_collision_effect_positions_debug():
    vehicle_properties = get_global_properties()
    vehicle_properties['print_vehicle_collision_effect_positions'] = not vehicle_properties['print_vehicle_collision_effect_positions']
    set_vehicle_property("print_vehicle_collision_effect_positions", vehicle_properties['print_vehicle_collision_effect_positions'])
    if vehicle_properties['print_vehicle_collision_effect_positions']:
        log_info("Collision Effect Positions Debug activated")
        send_event("vehicle.debugscript.render.start")
    else:
        log_info("Collision Effect Positions Debug deactivated")

# ToggleHealthbarDebug function
def toggle_healthbar_debug():
    vehicle_properties = get_global_properties()
    vehicle_properties['showHealthbarDebug'] = not vehicle_properties['showHealthbarDebug']
    set_vehicle_property("showHealthbarDebug", vehicle_properties['showHealthbarDebug'])
    if vehicle_properties['showHealthbarDebug']:
        log_info("Healthbar Debug activated")
        send_event("healthbar.debug.start")
    else:
        log_info("Healthbar Debug deactivated")
        send_event("healthbar.debug.stop")

# ToggleDamageTrackerDebug function
def toggle_damage_tracker_debug():
    vehicle_properties = get_global_properties()
    vehicle_properties['print_dmgtracker_debug'] = not vehicle_properties['print_dmgtracker_debug']
    set_vehicle_property("print_dmgtracker_debug", vehicle_properties['print_dmgtracker_debug'])
    if vehicle_properties['print_dmgtracker_debug']:
        log_info("Collision DamageTracker Debug activated")
    else:
        log_info("Collision DamageTracker Debug deactivated")

# Init function - Initializes the debug menu options
def init():
    vehicle_properties = get_global_properties()
    vehicle_properties['print_dmgtracker_debug'] = False
    vehicle_properties['print_nondmg_debug'] = False
    vehicle_properties['BoardingSwayDebugEnabled'] = True
    vehicle_properties['BoardingShakeOffEnabled'] = False
    vehicle_properties['print_vehicle_collision_effect_positions'] = False
    set_vehicle_property("BoardingSwayDebugEnabled", True)
    set_vehicle_property("BoardingShakeOffEnabled", False)
    
    # Register event handlers
    register_event_handler("BoardingEnableShakingOff", boarding_enable_sway_debug)
    register_event_handler("ToggleDamageTrackerDebug", toggle_damage_tracker_debug)
    register_event_handler("ToggleHealthbarDebug", toggle_healthbar_debug)
    register_event_handler("ToggleDeformDebug", toggle_deform_debug)
    register_event_handler("BoardingEnableLandDebug", boarding_enable_land_debug)
    register_event_handler("ToggleVehicleCollisionEffectPositionsDebug", toggle_vehicle_collision_effect_positions_debug)
    
    log_info("Debug menu initialized")

# BoardingDisableShakingOff function
def boarding_disable_shaking_off():
    log_info("Vehicle Debug Menu, BoardingDisableShakingOff")
    vehicle_properties = get_global_properties()
    vehicle_properties['BoardingShakeOffEnabled'] = False
    set_vehicle_property("BoardingShakeOffEnabled", False)

# BoardingEnableShakingOff function
def boarding_enable_shaking_off():
    log_info("Vehicle Debug Menu, BoardingEnableShakingOff")
    vehicle_properties = get_global_properties()
    vehicle_properties['BoardingShakeOffEnabled'] = True
    set_vehicle_property("BoardingShakeOffEnabled", True)

# BoardingDisableSwayDebug function
def boarding_disable_sway_debug():
    log_info("Vehicle Debug Menu, BoardingDisableSwayDebug")
    vehicle_properties = get_global_properties()
    vehicle_properties['BoardingSwayDebugEnabled'] = False
    set_vehicle_property("BoardingSwayDebugEnabled", False)

# ToggleNonDamageCollisionTrackerDebug function
def toggle_non_damage_collision_tracker_debug():
    vehicle_properties = get_global_properties()
    vehicle_properties['print_nondmg_debug'] = not vehicle_properties['print_nondmg_debug']
    set_vehicle_property("print_nondmg_debug", vehicle_properties['print_nondmg_debug'])
    if vehicle_properties['print_nondmg_debug']:
        log_info("Collision NonDamage Debug activated")
    else:
        log_info("Collision NonDamage Debug deactivated")

# BoardingDisableLandDebug function
def boarding_disable_land_debug():
    log_info("Vehicle Debug Menu, BoardingDisableLandDebug")
    vehicle_properties = get_global_properties()
    vehicle_properties['BoardingLandDebugEnabled'] = False
    set_vehicle_property("BoardingLandDebugEnabled", False)

# ToggleTireSizeDebug function
def toggle_tire_size_debug():
    vehicle_properties = get_global_properties()
    vehicle_properties['showTireSizeDebug'] = not vehicle_properties['showTireSizeDebug']
    set_vehicle_property("showTireSizeDebug", vehicle_properties['showTireSizeDebug'])
    if vehicle_properties['showTireSizeDebug']:
        log_info("Tire Size Debug activated")
        send_event("vehicle.debugscript.render.start")
    else:
        log_info("Tire Size Debug deactivated")

# ToggleGgDebug function
def toggle_gg_debug():
    vehicle_properties = get_global_properties()
    vehicle_properties['showGgDebug'] = not vehicle_properties['showGgDebug']
    set_vehicle_property("showGgDebug", vehicle_properties['showGgDebug'])
    if vehicle_properties['showGgDebug']:
        log_info("G-G Display activated")
        send_event("vehicle.debugscript.render.start")
    else:
        log_info("G-G Display deactivated")

# Run the initialization
init()
