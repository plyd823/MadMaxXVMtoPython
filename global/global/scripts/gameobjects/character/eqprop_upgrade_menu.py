class MenuScript:
    def __init__(self):
        self.scriptgo = None
        self.debug = None
        self.vector = None
        self.character = None
        self.selected_id = 0
        self.menu_level = 0
        self.menu_levels = []
        self.upgrade_names = []
        self.time_enabled = 0
        self.time_since_btn = 0
        self.wait_for_btn_release = False

    def set_vector(self, x, y, z):
        # Assuming this function sets some vector attribute
        self.vector = (x, y, z)

    def get_selected_id(self):
        return self.selected_id

    def get_menu_level(self):
        return self.menu_level

    def get_menu_index_limit(self):
        return len(self.menu_levels) - 1

    def set_selected_id(self, selected_id):
        self.selected_id = selected_id

    def go_enter(self):
        selected_id = self.get_selected_id()
        if self.menu_level == 0:
            self.selected_id += 1
        else:
            player = self.character.get_player()
            self.character.set_upgrade_level(selected_id)
        self.set_selected_id(0)  # Reset to 0 after the action

    def go_exit(self):
        if self.menu_level == 0:
            self.end_menu()
        else:
            self.menu_level = 0
        self.set_selected_id(0)

    def go_down(self):
        max_limit = self.get_menu_index_limit()
        current_id = self.get_selected_id()
        if current_id < max_limit:
            self.selected_id += 1
        else:
            self.selected_id = max_limit
        self.set_selected_id(self.selected_id)

    def go_up(self):
        max_limit = self.get_menu_index_limit()
        current_id = self.get_selected_id()
        if current_id > 0:
            self.selected_id -= 1
        else:
            self.selected_id = 0
        self.set_selected_id(self.selected_id)

    def print_upgrade_level(self):
        x = self.vector[0] + 0.19
        y = self.vector[1]
        self.set_vector(x, y, 0)
        # Draw upgrade level info (assumed function `draw_text`)
        self.debug.draw_text(f"Upgrade level: {self.character.get_upgrade_level()}")

    def update_render(self):
        self.time_enabled += 30  # Some kind of time-related operation
        # Assuming button input and state updates
        button_input = self.get_button_input()  # Placeholder function
        if button_input == 'enter':
            self.go_enter()
        elif button_input == 'exit':
            self.go_exit()
        elif button_input == 'down':
            self.go_down()
        elif button_input == 'up':
            self.go_up()

    def init(self):
        self.scriptgo = self.get_properties()
        self.set_selected_id(0)

    def debug_log(self):
        if self.debug_enabled:
            self.debug.log_info(f"Selected ID: {self.selected_id}, Menu Level: {self.menu_level}")
    
    # Helper functions for external calls
    def get_properties(self):
        # Returns some properties (pseudo code)
        return {}

    def get_button_input(self):
        # Placeholder method for button input
        return 'enter'

    def end_menu(self):
        # Placeholder for ending the menu
        print("End menu")

# Create instance and use
menu = MenuScript()
menu.set_vector(1, 1, 0)
menu.update_render()  # Example of updating render
