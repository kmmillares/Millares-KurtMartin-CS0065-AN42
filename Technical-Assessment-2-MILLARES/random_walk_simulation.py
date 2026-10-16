import agentpy as ap
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import Counter
import math


# ============================================================
# 1. AGENT DEFINITION
# ============================================================

class Walker(ap.Agent):

    def setup(self):
        # Store the complete path of the agent
        self.path = []

    def step(self):
        x, y = self.position

        # ----------------------------------------------------
        # Movement rule
        # ----------------------------------------------------
        if self.model.p.movement_rule == "avoid":

            # Possible directions
            directions = [
                (1, 0), (-1, 0),
                (0, 1), (0, -1),
                (0, 0)
            ]

            random.shuffle(directions)

            # Try to move to an unoccupied position
            new_position = self.position

            for dx, dy in directions:
                new_x = max(
                    0,
                    min(self.model.p.grid_size[0] - 1, x + dx)
                )
                new_y = max(
                    0,
                    min(self.model.p.grid_size[1] - 1, y + dy)
                )

                candidate = (new_x, new_y)

                # Check whether another agent is already there
                occupied = any(
                    other is not self
                    and other.position == candidate
                    for other in self.model.agents
                )

                if not occupied:
                    new_position = candidate
                    break

            self.position = new_position

        elif self.model.p.movement_rule == "preferred":

            # Preferred direction: move right
            preferred_direction = self.model.p.preferred_direction

            # Sometimes make a random move
            if random.random() < 0.7:
                dx, dy = preferred_direction
            else:
                dx, dy = random.choice([
                    (1, 0), (-1, 0),
                    (0, 1), (0, -1)
                ])

            new_x = max(
                0,
                min(self.model.p.grid_size[0] - 1, x + dx)
            )
            new_y = max(
                0,
                min(self.model.p.grid_size[1] - 1, y + dy)
            )

            self.position = (new_x, new_y)

        else:
            # Original random-walk rule
            dx, dy = random.choice([
                (1, 0), (-1, 0),
                (0, 1), (0, -1)
            ])

            new_x = max(
                0,
                min(self.model.p.grid_size[0] - 1, x + dx)
            )
            new_y = max(
                0,
                min(self.model.p.grid_size[1] - 1, y + dy)
            )

            self.position = (new_x, new_y)

        # Record new position
        self.path.append(self.position)


# ============================================================
# 2. MODEL DEFINITION
# ============================================================

class RandomWalkModel(ap.Model):

    def setup(self):

        # Create agents
        self.agents = ap.AgentList(
            self,
            self.p.agents,
            Walker
        )

        # Initialize random positions
        for agent in self.agents:

            agent.position = (
                random.randint(
                    0,
                    self.p.grid_size[0] - 1
                ),
                random.randint(
                    0,
                    self.p.grid_size[1] - 1
                )
            )

            # Record initial position
            agent.path.append(agent.position)

        # Create grid
        self.grid = ap.Grid(
            self,
            self.p.grid_size,
            torus=False
        )

        self.grid.add_agents(self.agents)

    def step(self):

        for agent in self.agents:
            agent.step()


# ============================================================
# 3. RUN SIMULATION
# ============================================================

num_agents = int(input("Enter number of agents: "))
grid_size = int(input("Enter grid size: "))
num_steps = int(input("Enter number of steps: "))

print("\nChoose movement rule:")
print("1 - Random")
print("2 - Avoid other agents")
print("3 - Preferred direction")

choice = input("Enter choice (1/2/3): ")

#Default value
preferred_direction = None

if choice == "2":
    movement_rule = "avoid"
elif choice == "3":
    movement_rule = "preferred"
    
    print("\nPreferred direction:")
    print("1 - Right")
    print("2 - Left")
    print("3 - Up")
    print("4 - Down")

    direction_choice = input("Choose direction: ")

    if direction_choice == "1":
        preferred_direction = (1, 0)
    elif direction_choice == "2":
        preferred_direction = (-1, 0)
    elif direction_choice == "3":
        preferred_direction = (0, 1)
    else:
        preferred_direction = (0, -1)
else:
    movement_rule = "random"


parameters = {
    "agents": num_agents,
    "grid_size": (grid_size, grid_size),
    "steps": num_steps,
    "movement_rule": movement_rule,
    "preferred_direction": preferred_direction
}


model = RandomWalkModel(parameters)
model.setup()


# ============================================================
# 4. ANIMATION WITH PATHS
# ============================================================

fig, ax = plt.subplots()

ax.set_xlim(0, grid_size)
ax.set_ylim(0, grid_size)

ax.set_xticks(range(grid_size + 1))
ax.set_yticks(range(grid_size + 1))

ax.grid(True)

# Scatter plot for agents
scat = ax.scatter([], [], s=150)

# One line for each agent
lines = []

for i in range(num_agents):

    line, = ax.plot([], [], linewidth=1)

    lines.append(line)


def update(frame):

    # Run one simulation step
    model.step()

    # Current positions
    x = [agent.position[0] for agent in model.agents]
    y = [agent.position[1] for agent in model.agents]

    scat.set_offsets(list(zip(x, y)))

    # Draw path of every agent
    for i, agent in enumerate(model.agents):

        path_x = [position[0] for position in agent.path]
        path_y = [position[1] for position in agent.path]

        lines[i].set_data(path_x, path_y)

    return [scat] + lines


ani = animation.FuncAnimation(
    fig,
    update,
    frames=num_steps,
    blit=True,
    repeat=False
)

plt.title(
    "Agent Movement - " +
    movement_rule.capitalize() +
    " Rule"
)

plt.show()


# ============================================================
# 5. FINAL POSITION ANALYSIS
# ============================================================

print("\n==============================")
print("FINAL POSITIONS")
print("==============================")

final_positions = []

for i, agent in enumerate(model.agents):

    position = agent.position

    final_positions.append(position)

    print(
        f"Agent {i + 1}: {position}"
    )


# ------------------------------------------------------------
# Count how many agents occupy each position
# ------------------------------------------------------------

position_counts = Counter(final_positions)

print("\n==============================")
print("POSITION DISTRIBUTION")
print("==============================")

for position, count in position_counts.items():

    print(
        f"Position {position}: "
        f"{count} agent(s)"
    )


# ------------------------------------------------------------
# Calculate average final position
# ------------------------------------------------------------

average_x = sum(
    position[0]
    for position in final_positions
) / num_agents

average_y = sum(
    position[1]
    for position in final_positions
) / num_agents


print("\nAverage final position:")
print(
    f"({average_x:.2f}, {average_y:.2f})"
)


# ------------------------------------------------------------
# Calculate spatial spread
# ------------------------------------------------------------

distances = []

for x, y in final_positions:

    distance = math.sqrt(
        (x - average_x) ** 2 +
        (y - average_y) ** 2
    )

    distances.append(distance)


average_distance = sum(distances) / num_agents

print(
    f"Average distance from center: "
    f"{average_distance:.2f}"
)


# ============================================================
# 6. FINAL POSITION PLOT
# ============================================================

plt.figure()

x = [p[0] for p in final_positions]
y = [p[1] for p in final_positions]

plt.scatter(x, y, s=150)

plt.xlim(0, grid_size)
plt.ylim(0, grid_size)

plt.xticks(range(grid_size + 1))
plt.yticks(range(grid_size + 1))

plt.grid(True)

plt.xlabel("X position")
plt.ylabel("Y position")

plt.title("Final Distribution of Agents")

plt.show()
