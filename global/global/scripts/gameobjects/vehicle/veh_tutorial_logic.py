class GameScript:
    def __init__(self):
        self.scriptgo = self.get_properties()
        self.max_boarder_jumping_slowmo = 0.0
        self.max_boarder_shake_off_slowmo = 0.0
        self.prompt_time_buffer = 0.0
        self.max_boarder_jumping_prompt = 3.0
        self.max_boarder_shake_off_prompt = 5.0
        self.prompt_boarder_jumping_slowmo_timeleft = 0.0
        self.prompt_boarder_shakeoff_slowmo_timeleft = 0.0

    def get_properties(self):
        # Assume it fetches properties from a game object
        return {}

    def check_slowmo_boarder_jumping(self):
        properties = self.get_properties()
        if self.max_boarder_jumping_slowmo > 0:
            game_object = self.get_game_object_by_alias("effect.sound.slowmo")
            if game_object:
                self.spawn_effect(game_object)
                self.log_info("boarder_slomo_triggered")
            self.max_boarder_jumping_slowmo -= 1
            self.prompt_boarder_jumping_slowmo_timeleft = 0.4

    def check_slowmo_boarder_shake_off(self):
        properties = self.get_properties()
        if self.max_boarder_shake_off_slowmo > 0:
            game_object = self.get_game_object_by_alias("effect.sound.slowmo")
            if game_object:
                self.spawn_effect(game_object)
                self.log_info("boarder_slomo_triggered")
            self.max_boarder_shake_off_slowmo -= 1
            self.prompt_boarder_shakeoff_slowmo_timeleft = 0.5

    def shakeoff_slowmo_speed(self):
        return 0.3

    def init(self):
        self.max_boarder_jumping_prompt = 3.0
        self.max_boarder_shake_off_prompt = 5.0
        self.prompt_time_buffer = 0.0
        self.max_boarder_jumping_slowmo = 0.0
        self.max_boarder_shake_off_slowmo = 0.0
        self.prompt_boarder_jumping_slowmo_timeleft = 0.0
        self.prompt_boarder_shakeoff_slowmo_timeleft = 0.0
        self.set_update_function(self.update)

    def check_prompt_boarder_jumping(self):
        properties = self.get_properties()
        if self.prompt_time_buffer >= 0:
            if self.max_boarder_jumping_prompt > 0:
                self.send_event("prompt_player_boarder_jumping")
                self.log_info("tutorial_triggered: prompt_player_boarder_jumping")
                self.max_boarder_jumping_prompt -= 1
                self.prompt_time_buffer = 2.0

    def jumping_slowmo_speed(self):
        return 0.2

    def check_prompt_boarder_shake_off(self):
        properties = self.get_properties()
        if self.prompt_time_buffer >= 0:
            if self.max_boarder_shake_off_prompt > 0:
                self.send_event("prompt_player_boarder_shake_off")
                self.log_info("tutorial_triggered: prompt_player_boarder_shake_off")
                self.max_boarder_shake_off_prompt -= 1
                self.prompt_time_buffer = 2.0

    def reset(self):
        self.init()

    def update(self):
        properties = self.get_properties()
        game_object = self.get_game_object_by_alias("effect.sound.slowmo")
        if game_object:
            self.stop_effect(game_object)

        if self.prompt_boarder_jumping_slowmo_timeleft > 0:
            self.prompt_boarder_jumping_slowmo_timeleft -= 1
            if self.prompt_boarder_jumping_slowmo_timeleft <= 0:
                self.stop_effect(game_object)

        if self.prompt_boarder_shakeoff_slowmo_timeleft > 0:
            self.prompt_boarder_shakeoff_slowmo_timeleft -= 1
            if self.prompt_boarder_shakeoff_slowmo_timeleft <= 0:
                self.stop_effect(game_object)

    def get_game_object_by_alias(self, alias):
        # Simulate fetching a game object by alias
        return {}

    def spawn_effect(self, game_object):
        # Simulate spawning an effect
        pass

    def stop_effect(self, game_object):
        # Simulate stopping an effect
        pass

    def send_event(self, event):
        # Simulate sending an event
        pass

    def log_info(self, message):
        print(message)

    def set_update_function(self, function):
        # Assume this sets a function to be called each frame
        self.update_function = function

# Example of usage
script = GameScript()
script.init()
script.check_slowmo_boarder_jumping()
script.check_slowmo_boarder_shake_off()
script.check_prompt_boarder_jumping()
script.check_prompt_boarder_shake_off()
script.update()
