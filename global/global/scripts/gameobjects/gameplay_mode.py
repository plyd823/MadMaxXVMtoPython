class Game:
    @staticmethod
    def SetBlackboardValueToObject(player, key, value):
        print(f"Set {key} to {value} for {player}")

    @staticmethod
    def GetCurrentActiveLocationDifficulty():
        return -1

    @staticmethod
    def GetRegionDifficultyForCharacter(player):
        return 3

    @staticmethod
    def GetTransform(obj):
        return {"r3": (0, 0, 0)}

class Character:
    @staticmethod
    def GetPlayer():
        return "Player"

    @staticmethod
    def GetVehicle(player):
        return "Vehicle" if player else None

    @staticmethod
    def IsObjectEqualTo(obj1, obj2):
        return obj1 == obj2

    @staticmethod
    def IsInSequence(player):
        return False

    @staticmethod
    def GetFloatRegister(player, register_id):
        return 0

    @staticmethod
    def SetFloatRegister(player, register_id, value):
        print(f"Set register {register_id} to {value}")

class ScriptGO:
    @staticmethod
    def SetUpdateFunction(obj, func_name):
        print(f"Set update function {func_name}")

    @staticmethod
    def GetProperties(obj):
        return {"time_since_combat_mode_activated": 0}


class GameDirector:
    @staticmethod
    def GetAiGameStateHashInRangeCount(state, range1, range2):
        return 0


class Vehicle:
    @staticmethod
    def GetNbVehicleEnemies(player, radius):
        return 0


def SetGameMode(mode):
    player = Character.GetPlayer()
    current_mode = mode
    if current_mode != mode:
        Game.SetBlackboardValueToObject(player, "13_3C_6C_8C", mode)


def Update():
    player = Character.GetPlayer()
    if not player:
        return

    properties = ScriptGO.GetProperties(None)
    time_since_combat_mode_activated = properties["time_since_combat_mode_activated"]

    if time_since_combat_mode_activated is None:
        time_since_combat_mode_activated = 0

    time_since_combat_mode_activated += 1

    if Character.IsInSequence(player):
        return

    if InVehicle():
        if VehicleEnemiesNear():
            return
        elif time_since_combat_mode_activated < 4:
            Exploration()
    else:
        OnGround()
        HandleAwareness(player)


def InVehicle():
    player = Character.GetPlayer()
    vehicle = Character.GetVehicle(player)
    if vehicle:
        return True
    return False


def OnGround():
    SetGameMode(1)


def Exploration():
    SetGameMode(1)


def HandleAwareness(player):
    enemies_near = GameDirector.GetAiGameStateHashInRangeCount("", 5, 0.75)
    if enemies_near > 0:
        Character.SetFloatRegister(player, 19, 1)
    else:
        Character.SetFloatRegister(player, 15, 1)


def VehicleEnemiesNear():
    player = Character.GetPlayer()
    vehicle = Character.GetVehicle(player)
    vehicle_position = Game.GetTransform(vehicle)["r3"]
    radius = 10
    enemy_count = Vehicle.GetNbVehicleEnemies(vehicle, radius)
    return enemy_count > 0


# Initialization
def Init():
    ScriptGO.SetUpdateFunction(None, "Update")
    player = Character.GetPlayer()
    Game.SetBlackboardValueToObject(player, "13_3C_6C_8C", 0)


# Run the initialization
Init()
Update()
