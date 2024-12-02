import random
import math

# Simulating the game and debug environment as placeholder functions
class Game:
    def GetGameObjectByAlias(self, alias):
        # Simulate getting a game object by alias
        return True  # Placeholder for actual game logic

class GarageState:
    def DebugSetUpgrade(self, upgrade_name, value):
        # Simulate setting an upgrade in the garage state
        print(f"Set upgrade: {upgrade_name} to {value}")

class Debug:
    def LogInfo(self, message):
        print(message)

# Placeholder for global game objects
game = Game()
debug = Debug()
garagestate = GarageState()

def mission1030UpgradeSetup():
    # Simulate getting the garage state
    garage_state = game.GetGameObjectByAlias("garage.state")
    
    if not garage_state:
        debug.LogInfo("UPGRADES MENU: no garage state")
        return

    # Upgrade attributes
    upgrades = [
        "ATT_RAMMING", "ATT_ARMOR", "ATT_BOARDING_DEFENSE", "ATT_HARPOON",
        "ATT_HARPOON_EXPLOSIVE", "ATT_TOP_SPEED", "ATT_BOOST", "ATT_ACCELERATION",
        "ATT_GRIP", "ATT_SUSPENSION", "ATT_WHEEL_ARMOR", "ATT_BODYWORK", 
        "ATT_DECAL", "ATT_HOOD_ORNAMENT", "ATT_REPAIR_SPEED"
    ]
    
    for upgrade in upgrades:
        # For this demo, the upgrade value is always 0, except for ATT_BOOST, which is 1
        value = 1 if upgrade == "ATT_BOOST" else 0
        garagestate.DebugSetUpgrade(upgrade, value)

def debugRandomizeUpgrades():
    # Simulate getting the garage state
    garage_state = game.GetGameObjectByAlias("garage.state")
    
    if not garage_state:
        debug.LogInfo("UPGRADES MENU: no garage state")
        return
    
    # Randomize upgrade values
    upgrades = [
        ("RAM", 6), ("ARMOR", 6), ("BOARDING_DEFENSE", 4), ("HARPOON", 7),
        ("HARPOON_EXPLOSIVE", 5), ("TOP SPEED", 6), ("BOOST", 5), ("ACCELERATION", 12),
        ("GRIP", 6), ("SUSPENSION", 6), ("WHEEL_ARMOR", 4), ("BODYWORK", 4),
        ("DECAL", 4), ("REPAIR_SPEED", 3)
    ]
    
    randomized_upgrades = {}
    
    for upgrade, multiplier in upgrades:
        value = math.ceil(random.random() * multiplier) - 1
        randomized_upgrades[upgrade] = value

    for upgrade, value in randomized_upgrades.items():
        garagestate.DebugSetUpgrade(upgrade, value)

def beefUpUpgrades():
    # Simulate getting the garage state
    garage_state = game.GetGameObjectByAlias("garage.state")
    
    if not garage_state:
        debug.LogInfo("UPGRADES MENU: no garage state")
        return

    # Set predefined upgrade values
    upgrades = {
        "ATT_RAMMING": 1, "ATT_ARMOR": 0, "ATT_HARPOON": 3, "ATT_HARPOON_EXPLOSIVE": 4,
        "ATT_TOP_SPEED": 0, "ATT_BOOST": 2, "ATT_ACCELERATION": 2, "ATT_GRIP": 2,
        "ATT_SUSPENSION": 0, "ATT_REPAIR_SPEED": 2
    }

    for upgrade, value in upgrades.items():
        garagestate.DebugSetUpgrade(upgrade, value)

def rammingLevel1():
    # Simulate getting the garage state
    garage_state = game.GetGameObjectByAlias("garage.state")
    
    if not garage_state:
        debug.LogInfo("UPGRADES MENU: no garage state")
        return

    # Set the "ATT_RAMMING" upgrade to 1
    garagestate.DebugSetUpgrade("ATT_RAMMING", 1)

def debugOpenUpgradeScreen():
    # Simulate sending events to the game system
    sendEvent("game_teleport_interceptor_to_camera", "")
    sendEvent("upg.vehicles.unlockallattributes", "")
    sendEvent("gui_event", "quit_to_event")
    sendEvent("gui_event", "fe_change_to_in_game_state")
    sendEvent("gui_event", "gui_debug_show_vehicle_upgrades")

def sendEvent(event_name, event_data):
    # Placeholder function for sending events to the game system
    print(f"Event sent: {event_name} with data: {event_data}")

def reducePlayerEnvironmentDamage():
    # Simulate reducing the player environment damage scale
    damage_scale = 0.25
    print(f"Player environment damage scale set to: {damage_scale}")
    
# Example usage of the functions
mission1030UpgradeSetup()
debugRandomizeUpgrades()
beefUpUpgrades()
rammingLevel1()
debugOpenUpgradeScreen()
reducePlayerEnvironmentDamage()
