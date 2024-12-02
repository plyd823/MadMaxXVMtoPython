# Unlocks the garage based on the garage state
def unlock_garage():
    # Get properties from scriptgo
    properties = scriptgo.GetProperties()

    # Get the garage state object
    garage_state = game.GetGameObjectByAlias("garage.state")

    # Unlock the garage using its state
    garagestate.UnlockGarage(garage_state, properties.type)


# Locks the garage based on the garage state and reason_string_id
def lock_garage():
    # Get properties from scriptgo
    properties = scriptgo.GetProperties()

    # Get the garage state object
    garage_state = game.GetGameObjectByAlias("garage.state")

    if properties.reason_string_id is None:
        # Lock the garage without a reason string
        garagestate.LockGarage(garage_state, properties.type, gui.MakeLocalizationHashFromTag(""))
    else:
        # Lock the garage with a reason string
        garagestate.LockGarage(
            garage_state, properties.type, gui.MakeLocalizationHashFromTag(properties.reason_string_id)
        )


# Simulated game, scriptgo, gui, and garagestate objects for demonstration purposes
class ScriptGO:
    @staticmethod
    def GetProperties():
        return {"type": "garage_type", "reason_string_id": "garage_lock_reason"}


class Game:
    @staticmethod
    def GetGameObjectByAlias(alias):
        return f"GarageStateObject[{alias}]"


class GUI:
    @staticmethod
    def MakeLocalizationHashFromTag(tag):
        return f"HashForTag[{tag}]"


class GarageState:
    @staticmethod
    def UnlockGarage(garage_state, garage_type):
        print(f"Garage '{garage_state}' unlocked with type '{garage_type}'.")

    @staticmethod
    def LockGarage(garage_state, garage_type, reason_hash):
        print(f"Garage '{garage_state}' locked with type '{garage_type}' and reason hash '{reason_hash}'.")


# Initialize simulated objects
scriptgo = ScriptGO()
game = Game()
gui = GUI()
garagestate = GarageState()

# Test the functions
unlock_garage()
lock_garage()
