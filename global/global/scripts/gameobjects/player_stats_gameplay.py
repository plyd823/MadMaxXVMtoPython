import math
import time


class PlayerStats:
    def __init__(self):
        self.fury_toggle = 0
        self.hit_counter = 0
        self.fury_kill_counter = 0
        self.difficulty_scaling = 0
        self.rank_points = 0
        self.in_fury_mode = False
        self.fury_stack_points = 0
        self.player_last_kill_health = 100
        self.enemies_killed_without_taking_damage_in_row = 0
        self.jawbreaker_buffer_timer = 0
        self.fury_kill_callout_buffer_timer = 0
        self.block_fury_bonus_callout_timer = 0
        self.fury_kill_count_keep_on_screen_timer = 0
        self.skill_count_keep_on_screen_timer = 0
        self.cstack_time0 = 0
        self.fury_activation_effect_timer_on_attacker = 0
        self.use_from_zero_to_fury_timer = 1
        self.from_zero_to_fury_timer = 0
        self.hit_count_freeze_timer = 0
        self.fury_mode_exit_timer = 30
        self.limb_breaking_counter = 0

    def get_player_stats(self):
        return self


class Game:
    def __init__(self):
        self.player_stats = PlayerStats()

    def post_event_none(self, event):
        print(f"Posting event: {event}")

    def send_intent_trigger(self, event):
        print(f"Intent trigger: {event}")

    def hydra_send_ground_combat_event(self):
        print("Sending ground combat event")

    def hydra_send_fury_end_event(self):
        print("Sending fury end event")

    def reset_hit_counter(self):
        print("Resetting hit counter")

    def activate_fury_mode(self):
        print("Activating Fury Mode")
        self.player_stats.in_fury_mode = True
        self.player_stats.fury_stack_points = 100

    def deactivate_fury_mode(self):
        print("Deactivating Fury Mode")
        self.player_stats.in_fury_mode = False
        self.player_stats.fury_stack_points = 0


game = Game()


# Event handlers
def fury_event_stop_fury_mode():
    player_stats = game.player_stats.get_player_stats()
    player_stats.fury_toggle = 0
    print("Fury mode stopped")


def fury_event_fury_strike():
    player_stats = game.player_stats.get_player_stats()
    player_stats.hit_counter += 1
    player_stats.hit_count_freeze_timer = 0.6
    print("Fury strike event triggered")


def fury_event_shatter():
    player_stats = game.player_stats.get_player_stats()
    player_stats.fury_stack_points += 20
    player_stats.hit_count_freeze_timer = 0.6
    print("Shatter event triggered")


def reduce_fury_small():
    player_stats = game.player_stats.get_player_stats()
    player_stats.in_fury_mode = False
    if player_stats.in_fury_mode:
        player_stats.fury_stack_points -= 150
        print("Fury stack reduced")
    else:
        player_stats.fury_stack_points = 0
        print("Fury stack reset")


def fury_mode_exit():
    player_stats = game.player_stats.get_player_stats()
    player_stats.in_fury_mode = False
    player_stats.fury_mode_exit_timer = 30
    print("Fury mode exited")


def fury_event_shotgun_kill():
    player_stats = game.player_stats.get_player_stats()
    player_stats.fury_stack_points += 5
    player_stats.hit_counter += 1
    print("Shotgun kill event triggered")


def fury_event_weapon_strike():
    player_stats = game.player_stats.get_player_stats()
    player_stats.fury_stack_points += 5
    player_stats.hit_counter += 1
    player_stats.hit_count_freeze_timer = 0.6
    print("Weapon strike event triggered")


def fury_event_limb_breaking_counter():
    player_stats = game.player_stats.get_player_stats()
    player_stats.fury_stack_points += 12
    player_stats.hit_count_freeze_timer = 0.6
    player_stats.hit_counter += 1
    print("Limb-breaking counter event triggered")


# Helper functions

def check_fury_mode(player_stats):
    if player_stats.fury_stack_points >= 100:  # Example threshold
        player_stats.in_fury_mode = True
        print("Entering Fury Mode")
    else:
        print("Not enough Fury Stack to enter Fury Mode")


def update_gui_values():
    print("Updating GUI values...")


def update_fury_effects():
    print("Updating fury effects...")


# Game event-related functions

def on_player_killed():
    print("Player killed! Checking for Fury-related triggers.")
    player_stats = game.player_stats.get_player_stats()
    if player_stats.fury_stack_points >= 100:
        print("Player is in Fury mode")
    else:
        print("Player is not in Fury mode")


def on_enemy_killed():
    print("Enemy killed! Updating stats.")
    player_stats = game.player_stats.get_player_stats()
    player_stats.fury_stack_points += 10
    player_stats.fury_kill_counter += 1
    print(f"Fury stack points: {player_stats.fury_stack_points}")


def on_hit():
    print("Hit detected! Checking Fury-related stats.")
    player_stats = game.player_stats.get_player_stats()
    player_stats.hit_counter += 1
    player_stats.fury_stack_points += 5
    check_fury_mode(player_stats)


# Timers & cooldowns

def apply_fury_activation_timer():
    print("Applying Fury activation timer.")
    player_stats = game.player_stats.get_player_stats()
    player_stats.fury_activation_effect_timer_on_attacker = time.time() + 5  # Fury activation lasts for 5 seconds


def check_and_apply_fury_effects():
    print("Checking and applying Fury effects.")
    player_stats = game.player_stats.get_player_stats()
    if time.time() < player_stats.fury_activation_effect_timer_on_attacker:
        print("Fury effects are active.")
    else:
        print("Fury effects have expired.")


# Update counters and timers

def update_event_timers():
    print("Updating event timers.")
    player_stats = game.player_stats.get_player_stats()
    if player_stats.jawbreaker_buffer_timer > 0:
        player_stats.jawbreaker_buffer_timer -= 1
    if player_stats.fury_kill_callout_buffer_timer > 0:
        player_stats.fury_kill_callout_buffer_timer -= 1
    if player_stats.block_fury_bonus_callout_timer > 0:
        player_stats.block_fury_bonus_callout_timer -= 1
    if player_stats.fury_kill_count_keep_on_screen_timer > 0:
        player_stats.fury_kill_count_keep_on_screen_timer -= 1
    if player_stats.skill_count_keep_on_screen_timer > 0:
        player_stats.skill_count_keep_on_screen_timer -= 1


def apply_fury_mode_exit_timer():
    print("Applying Fury Mode Exit timer.")
    player_stats = game.player_stats.get_player_stats()
    if player_stats.fury_mode_exit_timer > 0:
        player_stats.fury_mode_exit_timer -= 1
    if player_stats.fury_mode_exit_timer == 0:
        fury_mode_exit()


# Game loop simulation

def game_loop():
    while True:
        # Simulate various game events
        on_player_killed()
        on_enemy_killed()
        on_hit()

        # Apply Fury-related timers and effects
        apply_fury_activation_timer()
        check_and_apply_fury_effects()
        update_event_timers()
        apply_fury_mode_exit_timer()

        time.sleep(1)  # Sleep to simulate the passage of time


# Run the simulation
game_loop()
