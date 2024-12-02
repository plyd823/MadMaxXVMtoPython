class ScriptGo:
    def __init__(self):
        self.properties = {}
    
    def get_properties(self):
        return self.properties

    def post_event(self, event):
        # Placeholder for post_event functionality
        print(f"Event: {event}")

class Game:
    @staticmethod
    def get_max_health():
        return 100.0  # Example max health value

    @staticmethod
    def inflict_damage(value, *args):
        print(f"Inflicted Damage: {value}")
        for arg in args:
            print(f"Arg: {arg}")

class Math:
    @staticmethod
    def clamp(value, min_value, max_value):
        return max(min(value, max_value), min_value)

class Debug:
    @staticmethod
    def log_info(message):
        print(f"LogInfo: {message}")
    
    @staticmethod
    def draw_text_depth(*args):
        print(f"DrawTextDepth: {args}")

class Damagable:
    def __init__(self):
        self.health = 100.0
        self.max_health = 100.0
        self.accumulated_damage = 0.0
        self.recent_damage = 0.0
        self.invulnerable = False
        self.ignore_collision_if_destroyed = False
        self.debug_show_health = False
        self.accumulated_damage_amount_for_event = 0.0
        self.mirror_pct_health_damagable = 0.0

    def make_vulnerable(self):
        scriptgo = ScriptGo()
        scriptgo.get_properties()
        self.invulnerable = False
        print("Made vulnerable.")

    def apply_damage(self, damage):
        scriptgo = ScriptGo()
        properties = scriptgo.get_properties()

        # Checking for invulnerability
        if properties.get('invulnerable', False):
            print("Invulnerable, no damage applied.")
            return
        
        self.health -= damage
        self.accumulated_damage += damage
        self.health = Math.clamp(self.health, 0, self.max_health)
        print(f"Applied {damage} damage. New health: {self.health}")

        # Post event if health changes
        scriptgo.post_event("Health changed")

    def get_damage_pct(self):
        scriptgo = ScriptGo()
        properties = scriptgo.get_properties()

        health_pct = self.health / self.max_health
        return health_pct

    def destroy(self):
        scriptgo = ScriptGo()
        properties = scriptgo.get_properties()

        if properties.get('onDestroyDamagable', None) is not None:
            print("Destroying object with additional damage.")
            Game.inflict_damage(1000000, self)
        print("Destroyed object.")

    def force_destroy(self):
        scriptgo = ScriptGo()
        scriptgo.post_event("Force Destroyed")
        print("Force Destroyed.")

    def should_ignore_collision(self):
        scriptgo = ScriptGo()
        properties = scriptgo.get_properties()

        return self.ignore_collision_if_destroyed and self.health <= 0

    def init(self):
        scriptgo = ScriptGo()
        properties = scriptgo.get_properties()

        if properties.get('health') is None:
            self.health = 100.0
        if properties.get('maxHealth') is None:
            self.max_health = 100.0
        if properties.get('invulnerable') is None:
            self.invulnerable = False
        if properties.get('ignoreCollisionIfDestroyed') is None:
            self.ignore_collision_if_destroyed = False
        if properties.get('debugShowHealth') is None:
            self.debug_show_health = False
        if properties.get('accumulatedDamage') is None:
            self.accumulated_damage = 0.0

        print("Initialized object with default values.")

    def send_damage_events(self):
        scriptgo = ScriptGo()
        properties = scriptgo.get_properties()

        damage_pct = self.accumulated_damage / self.max_health
        if damage_pct >= 0.25:
            scriptgo.post_event("SendDamageEvents onDamage25pcnt")
        if damage_pct >= 0.5:
            scriptgo.post_event("SendDamageEvents onDamage50pcnt")
        if damage_pct >= 0.75:
            scriptgo.post_event("SendDamageEvents onDamage75pcnt")

    def restore_health(self):
        scriptgo = ScriptGo()
        properties = scriptgo.get_properties()

        self.health = self.max_health
        print(f"Health restored to max: {self.health}")

    def update_render_debug_health(self):
        scriptgo = ScriptGo()
        properties = scriptgo.get_properties()

        if self.debug_show_health:
            health_pct = self.health / self.max_health
            print(f"Render debug health: {health_pct * 100:.2f}%")

    def get_recent_damage_pct(self):
        scriptgo = ScriptGo()
        properties = scriptgo.get_properties()

        return self.recent_damage / self.max_health

    def make_invulnerable(self):
        scriptgo = ScriptGo()
        properties = scriptgo.get_properties()

        self.invulnerable = True
        print("Made invulnerable.")

    def is_destroyed(self):
        scriptgo = ScriptGo()
        properties = scriptgo.get_properties()

        return self.health <= 0

    def get_health_pct(self):
        scriptgo = ScriptGo()
        properties = scriptgo.get_properties()

        return self.health / self.max_health


# Example Usage
damagable = Damagable()
damagable.init()
damagable.apply_damage(30)
damagable.restore_health()
damagable.make_vulnerable()
damagable.apply_damage(50)
damagable.destroy()
damagable.send_damage_events()
damagable.update_render_debug_health()
