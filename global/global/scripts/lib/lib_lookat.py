import numpy as np

# Assuming some helper classes to abstract the game and character functionality.
class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def set(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        return self

    def __mul__(self, value):
        return Vector(self.x * value, self.y * value, self.z * value)

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"


class Character:
    def __init__(self):
        self.look_at_gain = 1.0
        self.look_at_valid_target_cos_angle = 0.9
        self.look_at_bone_weights = {}
        self.look_at_bone_limits = {}
        self.look_at_bone_blend_speeds = {}
        self.player = False

    def set_look_at_bone_weights(self, bone, weights):
        self.look_at_bone_weights[bone] = weights

    def set_look_at_bone_limits(self, bone, limits):
        self.look_at_bone_limits[bone] = limits

    def set_look_at_bone_blend_speeds(self, bone, speeds):
        self.look_at_bone_blend_speeds[bone] = speeds

    def set_look_at_gain(self, gain):
        self.look_at_gain = gain

    def get_player(self):
        return self.player

    def set_look_at_valid_target_cos_angle(self, angle):
        self.look_at_valid_target_cos_angle = angle

    def get_world_matrix(self):
        return np.identity(4)

    def get_look_at_target(self):
        return Vector(1, 1, 1)

    def get_player_state(self):
        return self.player


class Game:
    def __init__(self):
        self.objects = []

    def is_object_equal_to(self, obj1, obj2):
        return obj1 == obj2


class Debug:
    @staticmethod
    def print_value(value):
        print(f"Debug: {value}")

    @staticmethod
    def log_info(value):
        print(f"Log: {value}")

    @staticmethod
    def sphere(vector):
        print(f"Drawing sphere at {vector}")


def print_and_log(message):
    Debug.print_value(message)
    Debug.log_info(message)


def set_soft_in_medium_out_blend_speeds(character, game):
    bones = ["Spine", "Spine1", "Spine2", "Neck", "Head"]
    multipliers = [0.8, 0.8, 0.8, 0.9, 1.0]
    speeds = [3.2, 3.2, 3.2, 3.2, 3.2]
    
    for bone, multiplier, speed in zip(bones, multipliers, speeds):
        # Calculate the blend speed for each bone
        blend_speed = Vector(0.8, 0.6, 1.8) * multiplier * speed
        character.set_look_at_bone_blend_speeds(bone, blend_speed)

    print_and_log("using SetSoftInMediumOutBlendSpeeds!")


def set_medium_blend_speeds(character, game):
    bones = ["Spine", "Spine1", "Spine2", "Neck", "Head"]
    multipliers = [0.8, 0.8, 0.8, 0.9, 1.0]
    speeds = [6, 6, 6, 6, 6]
    
    for bone, multiplier, speed in zip(bones, multipliers, speeds):
        blend_speed = Vector(0.8, 0.6, 1.8) * multiplier * speed
        character.set_look_at_bone_blend_speeds(bone, blend_speed)

    print_and_log("using SetMediumBlendSpeeds!")


def draw_look_at_target_sphere(character, game):
    if character.get_player():
        matrix = character.get_world_matrix()
        target = character.get_look_at_target()
        transformed_target = matrix @ np.array([target.x, target.y, target.z, 1])[:3]
        transformed_target = Vector(*transformed_target)
        Debug.sphere(transformed_target)


def activate_look_at_if_within_valid_angle(character, game):
    cos_value = 0.9  # Just a placeholder value for simplicity
    if cos_value > character.look_at_valid_target_cos_angle:
        draw_look_at_target_sphere(character, game)
        if game.is_object_equal_to(character.get_player(), character):
            print_and_log("LookAt active for Max")
        else:
            print_and_log("LookAt active for npc(s)")

        if cos_value > 0.5:
            character.set_look_at_gain(1)


def set_use_mostly_head(character):
    # Adjust bone weights for LookAt behavior
    character.set_look_at_bone_weights("Spine", Vector(0.01, 0, 0))
    character.set_look_at_bone_weights("Spine1", Vector(0.01, 0.01, 0.1))
    character.set_look_at_bone_weights("Spine2", Vector(0.03, 0.02, 0.2))
    character.set_look_at_bone_weights("Neck", Vector(0.46, 0.36, 0.25))
    character.set_look_at_bone_weights("Head", Vector(0.65, 0.5, 0.3))

    character.set_look_at_bone_limits("Spine", Vector(0.1, -0.1, 0.01))
    character.set_look_at_bone_limits("Spine1", Vector(0.1, -0.1, 0.01))
    character.set_look_at_bone_limits("Spine2", Vector(0.2, -0.2, 0.05))
    character.set_look_at_bone_limits("Neck", Vector(0.3, -0.3, 0.4))
    character.set_look_at_bone_limits("Head", Vector(0.4, -0.4, 0.5))

    print_and_log("using SetUseMostlyHead!")


# Main function to simulate the script execution
def main():
    game = Game()
    character = Character()
    
    # Simulate some game state
    character.player = True  # Assuming the character is the player
    
    set_soft_in_medium_out_blend_speeds(character, game)
    set_medium_blend_speeds(character, game)
    activate_look_at_if_within_valid_angle(character, game)
    set_use_mostly_head(character)


if __name__ == "__main__":
    main()
