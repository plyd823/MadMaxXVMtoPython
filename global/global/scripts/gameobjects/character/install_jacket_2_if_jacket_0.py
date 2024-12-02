# Simulating the "visibleplayerupgrades" object and its methods
class VisiblePlayerUpgrades:
    def GetVisiblePlayerUpgradeLevel(self, upgrade_name):
        # Simulating a method that gets the upgrade level for the given upgrade
        upgrade_levels = {
            "armor": 0,  # Example upgrade levels
            "knuckleduster": 0,
        }
        return upgrade_levels.get(upgrade_name, 0)

    def DebugSetVisiblePlayerUpgrade(self, upgrade_name, level):
        # Simulating setting the upgrade level for debugging purposes
        print(f"Setting {upgrade_name} to level {level} for debugging.")

# Creating an instance of the class
visibleplayerupgrades = VisiblePlayerUpgrades()

def trigger():
    # Checking armor upgrade level
    upgrade_name = "armor"
    level = visibleplayerupgrades.GetVisiblePlayerUpgradeLevel(upgrade_name)
    
    if level != 0:
        visibleplayerupgrades.DebugSetVisiblePlayerUpgrade(upgrade_name, 2)

    # Checking knuckleduster upgrade level
    upgrade_name = "knuckleduster"
    level = visibleplayerupgrades.GetVisiblePlayerUpgradeLevel(upgrade_name)
    
    if level != 0:
        visibleplayerupgrades.DebugSetVisiblePlayerUpgrade(upgrade_name, 1)

# Call the trigger function
trigger()
