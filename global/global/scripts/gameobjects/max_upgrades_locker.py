# Function to unlock maximum upgrades
def unlock_max_upgrades():
    # Get properties from scriptgo
    properties = scriptgo.GetProperties()

    # Call the UnlockMaxUpgrades method of visibleplayerupgrades with the properties' type
    visibleplayerupgrades.UnlockMaxUpgrades(properties["type"])


# Function to lock maximum upgrades
def lock_max_upgrades():
    # Get properties from scriptgo
    properties = scriptgo.GetProperties()

    # Check if the reason_string_id is None
    if properties.get("reason_string_id") is None:
        # Lock max upgrades without a reason
        visibleplayerupgrades.LockMaxUpgrades(properties["type"], gui.MakeLocalizationHashFromTag(""))
    else:
        # Lock max upgrades with a specific reason
        reason_hash = gui.MakeLocalizationHashFromTag(properties["reason_string_id"])
        visibleplayerupgrades.LockMaxUpgrades(properties["type"], reason_hash)


# Simulated scriptgo, gui, and visibleplayerupgrades classes for demonstration purposes
class ScriptGO:
    @staticmethod
    def GetProperties():
        # Simulating properties with a type and reason_string_id
        return {"type": "example_type", "reason_string_id": "upgrade_locked_reason"}


class GUI:
    @staticmethod
    def MakeLocalizationHashFromTag(tag):
        # Simulate making a localization hash from a tag
        return f"hash_{tag}"


class VisiblePlayerUpgrades:
    @staticmethod
    def UnlockMaxUpgrades(upgrade_type):
        print(f"Unlocked maximum upgrades for type '{upgrade_type}'.")

    @staticmethod
    def LockMaxUpgrades(upgrade_type, reason_hash):
        print(f"Locked maximum upgrades for type '{upgrade_type}' with reason '{reason_hash}'.")


# Initialize simulated objects
scriptgo = ScriptGO()
gui = GUI()
visibleplayerupgrades = VisiblePlayerUpgrades()

# Test the unlock and lock functions
unlock_max_upgrades()  # Example usage
lock_max_upgrades()    # Example usage
