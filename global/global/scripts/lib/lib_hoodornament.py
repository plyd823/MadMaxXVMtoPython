# ActivateArmorUpgrades
def activate_armor_upgrades():
    fire_resistance = 0.2
    lib_vehicle_upgrades.ChangeFireResistance(fire_resistance)
    vehicle = vehicle.GetSignatureVehicle()
    collision = lib_entity_proxy.GetCollision(vehicle)
    
    if collision:
        collision.bytes = [0xD6, 0xCA, 0xD3, 0x3A]
        fire_resistance -= 0.1
        lib_entity_proxy.Call2(scriptgo, -0.1, -0.1)
    
    global_properties = vehicle.GetGlobalProperties()
    boarder_shakeoff = global_properties.boardershakeoff_upgrade_scale + 0.2
    global_properties.boardershakeoff_upgrade_scale = boarder_shakeoff
    
    if not fire_resistance:
        vehicle.ChangeStatBuffValue(0x35, 0x8D, 0x35, 0x8A, 1)

# DetermineUpgradeGroup
def determine_upgrade_group(upgrade_level):
    if upgrade_level in [1, 7, 8]:
        return 1
    elif upgrade_level in [4, 10]:
        return 2
    elif upgrade_level in [2, 9]:
        return 3
    elif upgrade_level in [3, 11, 12]:
        return 4
    elif upgrade_level in [5, 6, 13]:
        return 5
    else:
        print(f"HoodOrnament - Unable to determine upgrade group for level {upgrade_level}")
        return 1

# DeactivateArmorUpgrades
def deactivate_armor_upgrades():
    fire_resistance = -0.2
    lib_vehicle_upgrades.ChangeFireResistance(fire_resistance)
    vehicle = vehicle.GetSignatureVehicle()
    collision = lib_entity_proxy.GetCollision(vehicle)
    
    if collision:
        collision.bytes = [0xD6, 0xCA, 0xD3, 0x3A]
        fire_resistance += 0.1
        lib_entity_proxy.Call2(scriptgo, 0.1, 0.1)
    
    global_properties = vehicle.GetGlobalProperties()
    boarder_shakeoff = global_properties.boardershakeoff_upgrade_scale - 0.2
    global_properties.boardershakeoff_upgrade_scale = boarder_shakeoff
    
    if not fire_resistance:
        vehicle.ChangeStatBuffValue(0x35, 0x8D, 0x35, 0x8A, -1)

# ActivateWeaponsUpgrades
def activate_weapons_upgrades():
    vehicle = vehicle.GetSignatureVehicle()
    harpoon_data = lib_entity_proxy.GetHarpoonDataWeapon(vehicle)
    
    if harpoon_data:
        harpoon_data.reload_time_scale -= 0.1
        game.StateContainerDataHarpoonChangeReloadTimeScale(harpoon_data.reload_time_scale)
    
    gameplay_script = lib_entity_proxy.GetSignatureVehicleGameplayScript(vehicle)
    if gameplay_script:
        properties = scriptgo.GetProperties(gameplay_script)
        properties.flameFuelConsumptionRateScale += -0.2
    
    if not harpoon_data:
        vehicle.ChangeStatBuffValue(0x9E, 0x43, 0x3D, 0x2D, 1)

# ActivateRammingUpgrades
def activate_ramming_upgrades():
    vehicle = vehicle.GetSignatureVehicle()
    collision = lib_entity_proxy.GetCollision(vehicle)
    
    if collision:
        collision.bytes = [0x04, 0xFE, 0x2A, 0x6D]
        scriptgo.Call3(0.1, 0.1, 0.05)
    
    if not collision:
        vehicle.ChangeStatBuffValue(0x0B, 0xBC, 0xBB, 0x37, 1)

# DeactivateWeaponsUpgrades
def deactivate_weapons_upgrades():
    vehicle = vehicle.GetSignatureVehicle()
    harpoon_data = lib_entity_proxy.GetHarpoonDataWeapon(vehicle)
    
    if harpoon_data:
        harpoon_data.reload_time_scale += 0.1
        game.StateContainerDataHarpoonChangeReloadTimeScale(harpoon_data.reload_time_scale)
    
    gameplay_script = lib_entity_proxy.GetSignatureVehicleGameplayScript(vehicle)
    if gameplay_script:
        properties = scriptgo.GetProperties(gameplay_script)
        properties.flameFuelConsumptionRateScale -= -0.2
    
    if not harpoon_data:
        vehicle.ChangeStatBuffValue(0x9E, 0x43, 0x3D, 0x2D, -1)

# ActivateTractionUpgrades
def activate_traction_upgrades():
    lib_vehicle_upgrades.ChangeTireAdditionUpgrade(0.05)
    lib_vehicle_upgrades.ChangeMass(0)
    if not 0:
        vehicle.ChangeStatBuffValue(0x29, 0x16, 0x92, 0x78, 1)

# DeactivateRammingUpgrades
def deactivate_ramming_upgrades():
    vehicle = vehicle.GetSignatureVehicle()
    collision = lib_entity_proxy.GetCollision(vehicle)
    
    if collision:
        collision.bytes = [0x04, 0xFE, 0x2A, 0x6D]
        scriptgo.Call3(-0.1, -0.1, -0.05)
    
    if not collision:
        vehicle.ChangeStatBuffValue(0x0B, 0xBC, 0xBB, 0x37, -1)

# DeactivateHoodOrnamentUpgrade
def deactivate_hood_ornament_upgrade(level):
    if level == 0:
        upgrade_group = determine_upgrade_group(level)
        if upgrade_group == 1:
            deactivate_engine_upgrades()
        elif upgrade_group == 2:
            deactivate_traction_upgrades()
        elif upgrade_group == 3:
            deactivate_ramming_upgrades()
        elif upgrade_group == 4:
            deactivate_weapons_upgrades()
        else:
            deactivate_armor_upgrades()

# ActivateHoodOrnamentUpgrade
def activate_hood_ornament_upgrade(level):
    if level == 0:
        upgrade_group = determine_upgrade_group(level)
        if upgrade_group == 1:
            activate_engine_upgrades()
        elif upgrade_group == 2:
            activate_traction_upgrades()
        elif upgrade_group == 3:
            activate_ramming_upgrades()
        elif upgrade_group == 4:
            activate_weapons_upgrades()
        else:
            activate_armor_upgrades()

# ActivateEngineUpgrades
def activate_engine_upgrades():
    lib_vehicle_upgrades.ChangeAdditionalAccelerationScale(0.01)
    lib_vehicle_upgrades.ChangeAdditionalTopSpeed(0.025)
    if not 0:
        vehicle.ChangeStatBuffValue(0x55, 0x5B, 0x28, 0x1B, 1)

# DeactivateEngineUpgrades
def deactivate_engine_upgrades():
    lib_vehicle_upgrades.ChangeAdditionalAccelerationScale(-0.01)
    lib_vehicle_upgrades.ChangeAdditionalTopSpeed(-0.025)
    if not 0:
        vehicle.ChangeStatBuffValue(0x55, 0x5B, 0x28, 0x1B, -1)

# DeactivateTractionUpgrades
def deactivate_traction_upgrades():
    lib_vehicle_upgrades.ChangeTireAdditionUpgrade(-0.05)
    lib_vehicle_upgrades.ChangeMass(0)
    if not 0:
        vehicle.ChangeStatBuffValue(0x29, 0x16, 0x92, 0x78, -1)
