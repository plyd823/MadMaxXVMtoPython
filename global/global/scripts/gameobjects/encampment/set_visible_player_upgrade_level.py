class ScriptGo:
    def GetProperties(self):
        # Simulate the properties returned by the "GetProperties" method
        return {
            "is_tool": True,
            "is_perk": False,
            "attr_id": 123,
            "level": 5,
            "part_id": 45
        }

class VisiblePlayerUpgrades:
    def DebugSetTool(self, attr_id, level):
        # Simulate setting a tool upgrade
        print(f"Tool upgrade set: attr_id = {attr_id}, level = {level}")

    def DebugSetPerk(self, attr_id, level):
        # Simulate setting a perk upgrade
        print(f"Perk upgrade set: attr_id = {attr_id}, level = {level}")

    def DebugSetVisiblePlayerUpgrade(self, part_id, attr_id, level):
        # Simulate setting a visible player upgrade
        print(f"Visible upgrade set: part_id = {part_id}, attr_id = {attr_id}, level = {level}")

    def GetVisiblePlayerUpgradeLevel(self, part_id, attr_id):
        # Simulate getting the visible player upgrade level
        return 3  # Example return value for the upgrade level

# Instantiate the objects
scriptgo = ScriptGo()
visible_player_upgrades = VisiblePlayerUpgrades()

def trigger():
    # Step 1: Get properties from the 'scriptgo' object
    properties = scriptgo.GetProperties()

    # Step 2: Check if 'is_tool' is True
    if properties["is_tool"]:
        # Step 3: Retrieve 'attr_id' and 'level' from properties
        attr_id = properties["attr_id"]
        level = properties["level"]

        # Step 4: Compare level with 0 and call DebugSetTool if greater
        if level > 0:
            visible_player_upgrades.DebugSetTool(attr_id, level)
            return  # Exit after setting the tool
        else:
            return

    # Step 5: Check if 'is_perk' is True
    if properties["is_perk"]:
        # Step 6: Retrieve 'attr_id' and 'level' from properties
        attr_id = properties["attr_id"]
        level = properties["level"]

        # Step 7: Compare level with 0 and call DebugSetPerk if greater
        if level > 0:
            visible_player_upgrades.DebugSetPerk(attr_id, level)
            return  # Exit after setting the perk
        else:
            return

    # Step 8: Retrieve 'part_id' and 'attr_id' from properties
    part_id = properties["part_id"]
    attr_id = properties["attr_id"]
    level = properties["level"]

    # Step 9: Get the visible player upgrade level
    current_level = visible_player_upgrades.GetVisiblePlayerUpgradeLevel(part_id, attr_id)

    # Step 10: Check if the 'level' is less than 'current_level' and proceed
    if level <= current_level:
        # Step 11: Call DebugSetVisiblePlayerUpgrade if conditions are met
        visible_player_upgrades.DebugSetVisiblePlayerUpgrade(part_id, attr_id, level)

# Call the trigger function
trigger()
