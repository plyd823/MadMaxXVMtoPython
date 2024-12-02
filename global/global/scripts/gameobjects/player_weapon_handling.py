class Vehicle:
    def __init__(self):
        self.selected_go = None
        self.harpoon_active = False
        self.toggle_list = []
        self.toggle_index = 0
        self.last_sig_veh_index = 0
        self.input_quick_fire_held = False
        self.sideburner = None

    def get_properties(self):
        return self

    def get_player_vehicle(self):
        return self

    def get_harpoon(self):
        return self

    def is_signature_vehicle(self):
        return False

    def log_info(self, message):
        print(message)


class VehicleUpgrades:
    @staticmethod
    def get_harpoon_upgrade_level():
        return 0

    @staticmethod
    def get_sideburner_level():
        return 0


class Debug:
    @staticmethod
    def log_info(message):
        print(message)


# Mock external objects
scriptgo = Vehicle()
lib_vehicle = Vehicle()
lib_vehicleupgrades = VehicleUpgrades()
debug = Debug()


def quick_fire_held():
    properties = scriptgo.get_properties()
    selected_go = properties.selected_go

    if selected_go != scriptgo.selected_go:
        properties.selected_go = selected_go
        properties.input_quick_fire_held = True

        if properties.input_quick_fire_held:
            debug.log_info("player_weapon_handling: QuickFireHeld")


def select_harpoon():
    properties = scriptgo.get_properties()
    signature_vehicle_available = lib_vehicle.is_signature_vehicle()

    if signature_vehicle_available:
        harpoon_upgrade_level = lib_vehicleupgrades.get_harpoon_upgrade_level()

        if harpoon_upgrade_level > 0 and properties.harpoon_active:
            player_vehicle = lib_vehicle.get_player_vehicle()

            if player_vehicle is not None:
                if player_vehicle.is_signature_vehicle():
                    unselect_current_weapon()
                    harpoon = player_vehicle.get_harpoon()
                    properties.selected_go = harpoon
                    debug.log_info("player_weapon_handling: SelectHarpoon")


def switch_to_index():
    properties = scriptgo.get_properties()
    player_vehicle = lib_vehicle.get_player_vehicle()

    if player_vehicle is not None:
        if player_vehicle.is_signature_vehicle():
            properties.toggle_index = properties.toggle_list[properties.toggle_index]
            properties.last_sig_veh_index = properties.toggle_index


def side_burner_available():
    player_vehicle = lib_vehicle.get_player_vehicle()

    if player_vehicle is not None:
        sideburner = player_vehicle.get_harpoon()

        if sideburner is not None:
            signature_vehicle_available = player_vehicle.is_signature_vehicle()

            if signature_vehicle_available:
                sideburner_level = lib_vehicleupgrades.get_sideburner_level()

                if sideburner_level >= 0:
                    return True

    return False


def unselect_current_weapon():
    # Placeholder for unselecting current weapon
    pass


# Example usage:
quick_fire_held()
select_harpoon()
switch_to_index()
if side_burner_available():
    print("Sideburner is available.")
else:
    print("Sideburner is not available.")
