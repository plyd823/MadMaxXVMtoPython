class Game:
    objects = {}

    @staticmethod
    def GetGameObjectByAlias(alias):
        return Game.objects.get(alias)

    @staticmethod
    def RegisterObject(alias, obj):
        Game.objects[alias] = obj

    @staticmethod
    def InitTransformRecursively(entity, transform):
        print(f"Initializing transform recursively for {entity} with {transform}")

    @staticmethod
    def SendEvent(event, data):
        print(f"Event Sent: {event}, Data: {data}")

    @staticmethod
    def GetChildByIndex(obj, index):
        if 0 <= index < len(obj.children):
            return obj.children[index]
        return None

    @staticmethod
    def IsObjectEqualTo(obj1, obj2):
        return obj1 == obj2

    @staticmethod
    def GetNbChilds(obj):
        return len(obj.children)


class Debug:
    @staticmethod
    def LogInfo(message, *args):
        print(message % args)


class GameObject:
    def __init__(self, alias):
        self.alias = alias
        self.children = []
        self.properties = {
            "teleporting_mat": "default_matrix",
            "wait_time": 0.0,
            "isLoaded": False,
            "next_to_spawn": None
        }

    def GetProperties(self):
        return self.properties

    def SetUpdateFunction(self, func_name):
        print(f"Set update function: {func_name}")

    def AddChild(self, child):
        self.children.append(child)


class SpawnPoint(GameObject):
    def __init__(self, alias):
        super().__init__(alias)

    def UpdateSpawnPosition(self):
        Debug.LogInfo("Updated spawn position for %s", self.alias)


def UpdateTransformationOnSpawnedObject():
    spawned_entity = Game.GetGameObjectByAlias("debug_spawn_vehicle")
    if spawned_entity:
        Debug.LogInfo("Found spawned entity %s", spawned_entity.alias)
        Game.InitTransformRecursively(spawned_entity, spawned_entity.GetProperties()["teleporting_mat"])
    else:
        Debug.LogInfo("Failed to find spawned entity")


def UnloadAllSpawnLocationsExcept(exception_entity):
    Debug.LogInfo("Unloading all spawn locations except %s", exception_entity.alias)
    for obj in Game.objects.values():
        if obj != exception_entity:
            Debug.LogInfo("Despawning %s", obj.alias)


def UpdateSpawning(obj, delta_time):
    properties = obj.GetProperties()
    properties["wait_time"] += delta_time

    spawn_point = Game.GetGameObjectByAlias("debug_spawn_point")
    if spawn_point:
        Debug.LogInfo("Spawn point found: %s", spawn_point.alias)
        spawn_point.UpdateSpawnPosition()
        Game.SendEvent("spawn_team_entity", "")
    else:
        Debug.LogInfo("Failed to find a spawn point")


def Init(obj):
    properties = obj.GetProperties()
    properties["teleport_wait_time"] = 0.0
    properties["isLoaded"] = False
    properties["next_to_spawn"] = None

    Debug.LogInfo("Initializing game object %s", obj.alias)
    num_children = Game.GetNbChilds(obj)
    Debug.LogInfo("Number of children: %d", num_children)

    for index in range(num_children):
        child = Game.GetChildByIndex(obj, index)
        if child:
            Debug.LogInfo("Initializing child %d: %s", index, child.alias)


def StartSpawning(obj):
    properties = obj.GetProperties()
    properties["isLoaded"] = True
    properties["wait_time"] = 0.0

    Debug.LogInfo("Starting spawn process for %s", obj.alias)
    obj.SetUpdateFunction("UpdateSpawning")


def SpawnLatest(obj):
    properties = obj.GetProperties()
    next_to_spawn = properties["next_to_spawn"]

    if next_to_spawn:
        UnloadAllSpawnLocationsExcept(next_to_spawn)
        Debug.LogInfo("Spawning latest entity: %s", next_to_spawn.alias)
    else:
        Debug.LogInfo("No entity to spawn")


def StartLoading(obj):
    properties = obj.GetProperties()
    properties["isLoaded"] = False
    Debug.LogInfo("Start loading next location %s", obj.alias)

    next_to_spawn = properties["next_to_spawn"]
    if next_to_spawn:
        next_to_spawn_properties = next_to_spawn.GetProperties()
        next_to_spawn_properties["spawn_on_player"] = properties.get("spawn_on_player", False)
        Game.InitTransformRecursively(next_to_spawn, next_to_spawn_properties["teleporting_mat"])


# Example Initialization
def main():
    # Create GameObjects
    game_obj = GameObject("root_object")
    spawn_point = SpawnPoint("debug_spawn_point")
    spawned_entity = GameObject("debug_spawn_vehicle")

    # Register objects in Game
    Game.RegisterObject("debug_spawn_vehicle", spawned_entity)
    Game.RegisterObject("debug_spawn_point", spawn_point)

    # Initialize and simulate behaviors
    Init(game_obj)
    StartSpawning(game_obj)
    UpdateSpawning(game_obj, delta_time=1.0)
    SpawnLatest(game_obj)
    StartLoading(game_obj)


if __name__ == "__main__":
    main()
