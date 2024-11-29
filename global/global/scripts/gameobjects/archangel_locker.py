class Game:
    @staticmethod
    def GetGameObjectByAlias(alias):
        # Mock function to simulate retrieving a game object by alias.
        # In the actual implementation, this should return the correct game object.
        if alias == "garage.state":
            return GarageState()

class GarageState:
    def LockArchangels(self):
        print("Archangels locked.")

    def UnlockArchangels(self):
        print("Archangels unlocked.")


def lock_archangels():
    garage_state = Game.GetGameObjectByAlias("garage.state")
    if garage_state:
        garage_state.LockArchangels()


def unlock_archangels():
    garage_state = Game.GetGameObjectByAlias("garage.state")
    if garage_state:
        garage_state.UnlockArchangels()


# Example usage:
lock_archangels()  # Output: Archangels locked.
unlock_archangels()  # Output: Archangels unlocked.
