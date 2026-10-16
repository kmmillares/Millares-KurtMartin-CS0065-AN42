import random


# ==========================================
# Task 1: Set Up the Environment
# ==========================================

environment = {
    "A": "",
    "B": "",
    "C": ""
}


# Check if a room is dirty
def is_dirty(room):
    return environment[room].lower() == "dirty"


# Clean a room
def clean_room(room):
    environment[room] = "Clean"


# Display the environment as a text-based grid
def display_grid(agent_location):
    rooms = []

    for room in ["A", "B", "C"]:
        if room == agent_location:
            rooms.append(f"[{room}-Agent]")
        else:
            rooms.append(f"[{room}-{environment[room]}]")

    print("    ".join(rooms))


# Get initial states
environment["A"] = input("Is room A Dirty or Clean? ").capitalize()
environment["B"] = input("Is room B Dirty or Clean? ").capitalize()
environment["C"] = input("Is room C Dirty or Clean? ").capitalize()

print()


# ==========================================
# Task 2: Rule-Based Agent
# ==========================================

class Agent:

    def __init__(self):
        # Agent starts in room A
        self.location = "A"

    # Move to another room
    def move(self, room):
        self.location = room

    # Perceive and act
    def perceive_and_act(self):

        # RULE 1:
        # If the current room is dirty,
        # clean it and DO NOT move.
        if is_dirty(self.location):
            clean_room(self.location)
            return f"Room {self.location} has been cleaned."

        # RULE 2:
        # If the current room is clean,
        # find the dirty rooms.
        dirty_rooms = [
            room for room in environment
            if is_dirty(room)
        ]

        # If there are dirty rooms,
        # randomly choose ONE and move to it.
        if dirty_rooms:
            next_room = random.choice(dirty_rooms)
            self.move(next_room)
            return f"Moving to room {next_room}"

        # RULE 3:
        # If all rooms are clean, stay idle.
        return "All rooms are clean. Agent is idle."


# ==========================================
# Task 3: Run the Simulation
# ==========================================

steps = int(input("How many steps should the agent run? "))

print()

agent = Agent()

for step in range(1, steps + 1):

    print(f"Step {step}:")

    # Show state BEFORE action
    display_grid(agent.location)

    # Perform exactly ONE action
    action = agent.perceive_and_act()

    print(action)

    # Show state AFTER action
    display_grid(agent.location)

    print()