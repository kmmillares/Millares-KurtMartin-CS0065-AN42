# Task 1: Set Up the Environment

# Initialize two rooms using a dictionary
environment = {
    "A": "",
    "B": ""
}


# Function to check if a room is dirty
def is_dirty(room):
    return environment[room].lower() == "dirty"


# Function to clean a room
def clean_room(room):
    environment[room] = "Clean"


# Get the initial state of each room from the user
environment["A"] = input("Is room A Dirty or Clean? ").capitalize()
environment["B"] = input("Is room B Dirty or Clean? ").capitalize()

print()


# Task 2: Implement the Rule-Based Agent

class Agent:
    def __init__(self):
        # Agent starts in room A
        self.location = "A"

    # Move to the other room
    def move(self):
        if self.location == "A":
            self.location = "B"
        else:
            self.location = "A"

    # Perceive and act based on the rules
    def perceive_and_act(self):
        # Rule 1: If the current room is dirty, clean it
        if is_dirty(self.location):
            clean_room(self.location)
            return "Room has been cleaned."

        # Rule 2: If the current room is clean, move to the other room
        else:
            self.move()
            return f"Moving to room {self.location}"


# Task 3: Run the Simulation

# Ask the user how many steps to run
steps = int(input("How many steps should the agent run? "))

print()

# Create the agent
agent = Agent()

# Run the simulation
for step in range(1, steps + 1):

    print(f"Step {step}: Agent is in room {agent.location}")

    # Agent perceives the environment and takes an action
    action = agent.perceive_and_act()

    print(action)
    print(f"Environment state: {environment}")
    print()