class ScriptGo:
    def GetProperties(self):
        # Simulate the properties returned by the "GetProperties" method
        return {
            "should_show": 0.0,  # Simulating a float value
            "attr_id": 123,      # Simulate an attribute ID
            "level": 5           # Simulate a level value
        }

class VisiblePlayerUpgrades:
    def SetUpgradeLevelShown(self, attr_id, level):
        # Simulate setting an upgrade level shown
        print(f"Upgrade shown: attr_id = {attr_id}, level = {level}")

# Instantiate the objects
scriptgo = ScriptGo()
visible_player_upgrades = VisiblePlayerUpgrades()

def trigger():
    # Step 1: Get properties from the 'scriptgo' object
    properties = scriptgo.GetProperties()

    # Step 2: Check if 'should_show' is not equal to 0.0
    if properties["should_show"] != 0.0:
        # Step 3: Retrieve 'attr_id' and 'level' from properties
        attr_id = properties["attr_id"]
        level = properties["level"]

        # Step 4: Set the upgrade level using the 'SetUpgradeLevelShown' method
        visible_player_upgrades.SetUpgradeLevelShown(attr_id, level)

# Call the trigger function
trigger()
