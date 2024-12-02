class Mission:
    def IsMissionActivated(self):
        # Simulating whether the mission is activated or not
        return True  # Replace with actual check
    
    def IsMissionCompleted(self):
        # Simulating whether the mission is completed or not
        return False  # Replace with actual check

class ScriptGo:
    def SendEvent(self, event_data):
        # Simulating sending an event
        print(f"Event sent: {event_data}")

# Creating instances of the classes
mission = Mission()
scriptgo = ScriptGo()

def trigger():
    # Check if the mission is activated and completed
    is_activated = mission.IsMissionActivated()
    is_completed = mission.IsMissionCompleted()
    
    # Perform logical NOT and AND operations on the mission status
    condition = is_activated and not is_completed
    
    # Trigger different events based on the condition
    if condition:
        # Equivalent to sending the event "CF E9 BE C4" (event 1)
        scriptgo.SendEvent("CF E9 BE C4")
    else:
        # Equivalent to sending the event "0D 74 CE 63" (event 2)
        scriptgo.SendEvent("0D 74 CE 63")

# Call the trigger function
trigger()
