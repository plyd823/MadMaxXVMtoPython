class Game:
    def __init__(self):
        self.garage_state = None
        self.vehicle = None

    def get_game_object_by_alias(self, alias):
        # Simulate getting a game object by alias
        if alias == "garage.state":
            return self.garage_state
        elif alias == "vehicle":
            return self.vehicle
        return None

    def log_info(self, message):
        print(f"INFO: {message}")

    def log_error(self, message):
        print(f"ERROR: {message}")

class GarageState:
    def __init__(self):
        self.upgrade_levels = {
            'armor': 0,
            'acceleration': 0,
            'boarding_defense': 0,
            'boost': 0,
            'suspension': 0,
            'explosive_harpoon': 0,
            'wheel_armor': 0,
            'ramming': 0,
            'bodywork': 0,
        }

    def get_upgrade_level(self, upgrade_type):
        return self.upgrade_levels.get(upgrade_type, 0)

class Vehicle:
    def __init__(self):
        self.axles = 2
        self.front_axle_to_com_distance = 1.0
        self.rear_axle_to_com_distance = 1.5
        self.suspension_spring_strength = [3000, 3000]

    def clear_all_tire_parameters(self):
        print("Cleared all tire parameters.")

    def get_signature_vehicle(self):
        return self

    def get_properties(self):
        return {'upgradeLevel': 0}


def get_upgrade_level(game, upgrade_type):
    garage_state = game.get_game_object_by_alias("garage.state")
    if not garage_state:
        game.log_info("UPGRADES MENU: no garage state")
        return 0
    return garage_state.get_upgrade_level(upgrade_type)


def get_boost_enabled(game):
    return get_upgrade_level(game, 'boost')


def change_tire_grip(vehicle):
    vehicle.clear_all_tire_parameters()
    tire_friction = vehicle.get_signature_vehicle().get_properties()
    tire_friction['upgradeLevel'] = 0


def mass_compensate_suspension_length(vehicle):
    front_axle_to_com = vehicle.front_axle_to_com_distance
    rear_axle_to_com = vehicle.rear_axle_to_com_distance
    axles = vehicle.axles
    suspension_spring_strength = vehicle.suspension_spring_strength

    # Perform suspension calculation (simplified version of the original code logic)
    if axles > 2:
        print("MassCompensateSuspensionLength doesn't support vehicles with more than 2 axles")
        return

    suspension_strength = sum(suspension_spring_strength)
    gravity_effect = 9.81

    length_factor = (front_axle_to_com + rear_axle_to_com) / 2
    suspension_max_length = suspension_strength * length_factor / gravity_effect

    print(f"Calculated suspension max length: {suspension_max_length}")


# Example usage:

# Setup game objects
game = Game()
game.garage_state = GarageState()
game.vehicle = Vehicle()

# Example: Fetching upgrade levels
armor_level = get_upgrade_level(game, 'armor')
acceleration_level = get_upgrade_level(game, 'acceleration')
boost_enabled = get_boost_enabled(game)

print(f"Armor Upgrade Level: {armor_level}")
print(f"Acceleration Upgrade Level: {acceleration_level}")
print(f"Boost Enabled: {boost_enabled}")

# Example: Changing tire grip
change_tire_grip(game.vehicle)

# Example: Mass compensating suspension length
mass_compensate_suspension_length(game.vehicle)
