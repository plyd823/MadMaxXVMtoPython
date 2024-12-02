import time

class Input:
    """Mock Input class to simulate button and gamepad input behavior."""
    def __init__(self):
        self.buttons = {
            'A': False,
            'B': False,
            'X': False,
            'Y': False,
        }
        self.gamepad_active = False

    def get_button_input(self, button):
        return self.buttons.get(button, False)
    
    def is_button_clicked(self, button):
        # Simulate button clicked event
        return self.get_button_input(button)
    
    def is_button_released(self, button):
        # Simulate button release event
        return not self.get_button_input(button)

    def get_button_hold_time(self, button):
        # Simulate the hold time for a button (in seconds)
        return 0.15
    
    def is_using_gamepad(self):
        return self.gamepad_active
    
    def set_button_state(self, button, state):
        self.buttons[button] = state


class ScriptGo:
    """Mock ScriptGo class to simulate calling methods on script."""
    def __init__(self):
        self.weapon_handling = {}

    def call(self, bytes_code):
        # Simulate script call using bytes code.
        print(f"Calling script with bytes: {bytes_code}")
    
    def get_properties(self):
        # Simulate returning script properties
        return self.weapon_handling


class WeaponHandling:
    """Simulate the weapon handling system."""
    def __init__(self):
        self.weapon = None
    
    def call_weapon_action(self, action_bytes):
        print(f"Weapon action: {action_bytes}")


# Main game loop functions
def fury_input(input_system):
    if input_system.get_button_input("A") > 0:
        return True
    return False

def check_weapon_selection(input_system, scriptgo):
    scriptgo.get_properties()
    if input_system.is_button_clicked("A"):
        scriptgo.call(b'\xD7\x50\x19\x61')
    
    if input_system.is_button_clicked("B"):
        scriptgo.call(b'\x46\x47\x10\xBE')

    if input_system.is_button_clicked("X"):
        scriptgo.call(b'\x66\x25\xEB\x29')

    if input_system.is_button_clicked("Y"):
        scriptgo.call(b'\xF5\x06\x45\x7C')

def check_weapon_input(input_system, scriptgo):
    scriptgo.get_properties()

    if input_system.is_using_gamepad():
        if input_system.get_button_input("A") > 0:
            scriptgo.call(b'\x61\x18\x9C\x2E')
        else:
            scriptgo.call(b'\xB0\x6C\xEF\x46')
    else:
        if input_system.get_button_input("A") > 0:
            scriptgo.call(b'\x61\x18\x9C\x2E')
        else:
            scriptgo.call(b'\xB0\x6C\xEF\x46')
        
    if input_system.is_button_clicked("B"):
        scriptgo.call(b'\x56\x6C\x45\xCE')

    if input_system.is_button_released("B"):
        scriptgo.call(b'\xE6\xE8\xD5\xE5')

def sprint_trigger_limit():
    return 0.2


# Example usage:
input_system = Input()
scriptgo = ScriptGo()
weapon_handling = WeaponHandling()

input_system.set_button_state("A", True)  # Simulate pressing button A

fury_result = fury_input(input_system)
print(f"FuryInput result: {fury_result}")

check_weapon_selection(input_system, scriptgo)

check_weapon_input(input_system, scriptgo)

sprint_limit = sprint_trigger_limit()
print(f"Sprint Trigger Limit: {sprint_limit}")
