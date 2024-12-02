class Game:
    def __init__(self):
        self.Actonenter = None
        self.Actonexit = None

    def do_act(self):
        # Simulates the DoAct method.
        print("Action performed")

    def enter(self, obj0, obj1):
        self._do_action(obj0, obj1, "Actonenter")

    def exit(self, obj0, obj1):
        self._do_action(obj0, obj1, "Actonexit")

    def _do_action(self, obj0, obj1, action_name):
        action = getattr(obj1, action_name, None)
        if action:
            action()
            self.do_act()
        else:
            print(f"No action found for {action_name}")

# Example usage:
class SomeObject:
    def Actonenter(self):
        print("Enter action triggered!")

    def Actonexit(self):
        print("Exit action triggered!")

# Create a game instance
game = Game()

# Example objects for the parameters
obj0 = SomeObject()  # This would be the first parameter in the XVM code
obj1 = SomeObject()  # This would be the second parameter in the XVM code

# Trigger the Enter and Exit actions
game.enter(obj0, obj1)
game.exit(obj0, obj1)
