import math

# Class to represent player stats
class PlayerStats:
    def __init__(self):
        self.rank = 0.0
        self.rank_points = 0.0
        self.rank_kills = 0.0
        self.location_difficulty_override = 0.0
        self.real_difficulty = 0.0
        self.attack_slot_frequency_at_max_pressure_on_max_difficulty = 0.25
        self.attack_slot_frequency_at_max_pressure_on_min_difficulty = 2.5
        self.attack_slot_frequency_at_min_pressure_on_max_difficulty = 0.5
        self.attack_slot_frequency_at_min_pressure_on_min_difficulty = 2.75
        self.attack_slot_frequency_random_add = 0.5
        self.min_pressure = 30
        self.max_pressure = 130
        self.enemy_attack_speed_at_min_difficulty = 0.85
        self.enemy_attack_speed_at_max_difficulty = 1.15
        self.difficulty_scaling_boarding = 0.5


# Class to represent script properties and functions
class ScriptGo:
    def __init__(self):
        self.debug_render = False

    def set_render_function(self, func):
        pass

    def set_update_function(self, func):
        pass

    def get_properties(self):
        return self


# Global instances
playerstats = PlayerStats()
scriptgo = ScriptGo()


# Utility Functions
def clamp(value, min_val, max_val):
    return max(min(value, max_val), min_val)


# Functions
def set_rank_to_min():
    playerstats.rank = 0.0


def set_rank_to_max():
    playerstats.rank = 1.0


def set_rank_to_default():
    playerstats.rank = 0.5
    playerstats.rank_points = 0.0
    playerstats.rank_kills = 0.0


def increase_rank():
    playerstats.rank = clamp(playerstats.rank + 0.1, 0.0, 1.0)


def decrease_rank():
    playerstats.rank = clamp(playerstats.rank - 0.1, 0.0, 1.0)


def set_difficulty_level(level):
    playerstats.location_difficulty_override = level


def reset_difficulty():
    playerstats.real_difficulty = 0.0
    playerstats.location_difficulty_override = 0.0
    set_rank_to_default()


def rank_update():
    if playerstats.rank_kills >= 10:
        if playerstats.rank_points > 0:
            rank_modifier = (math.log10(playerstats.rank_points + 7) * 20 - 16.9) / 100
        else:
            rank_modifier = (math.log10(playerstats.rank_points + 7) * 20 - 16.9) / 50

        do_rank_update(rank_modifier)


def do_rank_update(modifier):
    playerstats.rank = clamp(playerstats.rank + modifier, 0.0, 1.0)
    playerstats.rank_points = 0
    playerstats.rank_kills = 0


def write_tweak_values_to_player_stats():
    playerstats.attack_slot_frequency_at_max_pressure_on_max_difficulty = 0.25
    playerstats.attack_slot_frequency_at_max_pressure_on_min_difficulty = 2.5
    playerstats.attack_slot_frequency_at_min_pressure_on_max_difficulty = 0.5
    playerstats.attack_slot_frequency_at_min_pressure_on_min_difficulty = 2.75
    playerstats.attack_slot_frequency_random_add = 0.5
    playerstats.min_pressure = 30
    playerstats.max_pressure = 130
    playerstats.enemy_attack_speed_at_min_difficulty = 0.85
    playerstats.enemy_attack_speed_at_max_difficulty = 1.15
    playerstats.difficulty_scaling_boarding = 0.5


def on_player_killed():
    playerstats.rank_points = 0.0
    playerstats.rank_kills = 0.0
    playerstats.rank = clamp(playerstats.rank - 0.4, 0.0, 1.0)


def debug_show_ui():
    scriptgo.debug_render = True
    scriptgo.set_render_function(render)


def debug_hide_ui():
    scriptgo.debug_render = False
    scriptgo.set_render_function(None)


def render():
    if scriptgo.debug_render:
        print(f"RealDifficulty: {playerstats.real_difficulty}")
        print(f"LocationDifficulty: {playerstats.location_difficulty_override}")
        print(f"Rank: {playerstats.rank}")
        print(f"RankPoints: {playerstats.rank_points}")
        print(f"RankKills: {playerstats.rank_kills}")


def init():
    reset_state()
    scriptgo.set_update_function(update)


def reset_state():
    write_tweak_values_to_player_stats()
    reset_difficulty()


def update():
    pass


# Initialize the game
init()
