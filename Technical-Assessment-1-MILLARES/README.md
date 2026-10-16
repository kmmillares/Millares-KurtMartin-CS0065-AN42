
# Random Walk Simulation Using AgentPy

This repository contains the output for Technical Assessment 1 (TA1) for CS0065 – Intelligent Systems. The project implements a random walk simulation using Python and AgentPy, where multiple agents move randomly within a grid-based environment.

The simulation demonstrates how agents move over time, follow different movement rules, and remain within the boundaries of the grid. It also visualizes agent paths and analyzes their final positions and spatial distribution.

## Features

- **Random Movement** – Agents move randomly in one of four directions: up, down, left, or right.
- **Collision Avoidance** – Agents attempt to move to unoccupied positions.
- **Preferred Direction** – Agents can favor a selected direction while retaining some random movement.
- **Path Visualization** – Displays the movement paths of individual agents.
- **Final Position Analysis** – Reports the final position of each agent and the distribution of agents across the grid.
- **Spatial Distribution Visualization** – Displays the final positions of agents on a grid.

## Files

- `TA1_Millares.pdf` – Technical assessment report containing the background, source code, simulation instructions, and answers to the laboratory questions.
- `random_walk.py` – Python script for running the random walk simulation. *(Use the actual filename of your Python script if it differs.)*

## Technologies Used

- Python 3.x
- AgentPy
- Matplotlib

## Requirements

Make sure Python 3.x is installed on your computer. Install the required libraries using:

```bash
pip install agentpy matplotlib
```

## How to Run

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run the Python script:

   ```bash
   python random_walk.py
   ```

4. Enter the requested simulation parameters:
   - Number of agents
   - Grid size
   - Number of steps
5. Select a movement rule:
   - `1` – Random movement
   - `2` – Avoid other agents
   - `3` – Preferred direction
6. If you select preferred direction, choose right, left, up, or down.
7. Observe the animation and review the final position analysis and distribution plot.

## Simulation Objectives

- Understand the concept of random walks in a grid environment.
- Implement a multi-agent simulation using Python and AgentPy.
- Visualize agent movement and paths over time.
- Compare the effects of different movement rules and simulation parameters.
- Analyze the final positions and spatial distribution of agents.

## Author

**Kurt Martin M. Millares**

## Course and Section

- **Course:** CS0065 – Intelligent Systems
- **Section:** BSCSSE – AN42
- **Professor:** Ms. Crisola Tan
- **Assessment:** Technical Assessment 1 (TA1)
