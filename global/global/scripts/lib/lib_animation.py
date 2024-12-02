class Game:
    def __init__(self):
        self.blackboard = {}
        self.animation = Animation()
        self.debug = Debug()
    
    def set_blackboard_value(self, key, value):
        self.blackboard[key] = value
        
    def get_blackboard_value(self, key):
        return self.blackboard.get(key, None)


class Animation:
    def get_time(self):
        return 1.0  # example value
    
    def get_sampler(self):
        return Sampler()

    def get_segment_info(self):
        return SegmentInfo()


class Sampler:
    def __init__(self):
        self.length = 10.0  # example value
        self.time = 2.0     # example value


class SegmentInfo:
    def __init__(self):
        self.length = 5.0


class Debug:
    @staticmethod
    def log_info(message):
        print(f"DEBUG: {message}")
    
    @staticmethod
    def draw_text_3d(text, position):
        print(f"3D Text: {text} at {position}")


# Functions

def reset_additive_loop_counter(game):
    game.set_blackboard_value("1B B5 18 B4", 0.0)
    game.animation.get_time()  # Call to animation time, to match XVM's behavior


def debug_print_loop_counter(game):
    value = game.get_blackboard_value("1B B5 18 B4")
    transform = game.animation.get_time()
    loops = value  # Example computation
    debug_message = f"Loops: {loops}"
    game.debug.draw_text_3d(debug_message, (0, 0, 0))


def set_continuing_loop_count(game, obj0, obj1):
    segment = game.animation.get_segment_info()
    normalization_segment = segment.length
    time = game.animation.get_time()
    floor_value = int(time // normalization_segment)  # equivalent to floor() in XVM
    game.set_blackboard_value("1B B5 18 B4", floor_value)


def get_animation_time_normalized_to_full_body(game, obj0):
    segment = game.animation.get_segment_info()
    segment_length = segment.length
    time = game.animation.get_time()
    normalized_time = time / segment_length
    return normalized_time


def set_additive_loop_timer(game):
    game.set_blackboard_value("3D 20 F3 07", game.animation.get_time())


def set_sampler_times_if_doing_navigation_reentering(game, obj0, obj1):
    value = game.get_blackboard_value("61 72 F5 2A")
    if value > -0.1:
        sampler = game.animation.get_sampler()
        length = sampler.length
        time = sampler.time
        game.set_blackboard_value("61 72 F5 2A", time + length)


def get_additive_normalization_segment(game):
    segment_info = game.animation.get_segment_info()
    return segment_info


def reset_navigation_reentering_if_not_in_segment(game):
    # Assuming IsWithinSegmentSync() returns a boolean
    in_segment = False  # This would be replaced by the actual segment check
    if not in_segment:
        game.set_blackboard_value("61 72 F5 2A", -1)


def increase_additive_loop_counter(game):
    time = game.animation.get_time()
    prev_value = game.get_blackboard_value("3D 20 F3 07")
    delta_time = time - prev_value
    if delta_time > 0:
        game.set_blackboard_value("1B B5 18 B4", prev_value + delta_time)


# Example usage
game = Game()

reset_additive_loop_counter(game)
debug_print_loop_counter(game)

obj0 = None  # Placeholder for object 0
obj1 = None  # Placeholder for object 1

set_continuing_loop_count(game, obj0, obj1)
normalized_time = get_animation_time_normalized_to_full_body(game, obj0)
set_additive_loop_timer(game)
set_sampler_times_if_doing_navigation_reentering(game, obj0, obj1)

get_additive_normalization_segment(game)
reset_navigation_reentering_if_not_in_segment(game)
increase_additive_loop_counter(game)
