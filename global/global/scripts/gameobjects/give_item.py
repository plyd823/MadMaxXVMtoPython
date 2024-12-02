# Function to give an item to the player or game object
def give_item():
    # Get properties from scriptgo
    properties = scriptgo.GetProperties()

    # Get the item name from the properties
    item_name = properties.item_name

    # Send an event to the game to give the item
    game.SendEvent("give_item", item_name)


# Simulated scriptgo and game objects for demonstration purposes
class ScriptGO:
    @staticmethod
    def GetProperties():
        # Simulating properties with an item name
        return {"item_name": "example_item"}


class Game:
    @staticmethod
    def SendEvent(event_name, item_name):
        print(f"Event '{event_name}' triggered to give item '{item_name}'.")


# Initialize simulated objects
scriptgo = ScriptGO()
game = Game()

# Test the give_item function
give_item()
