
# Technical Assessment 2: Rule-Based Agent

This repository contains the output for Technical Assessment 2 (TA2) for CS0065 – Intelligent Systems. The project implements a rule-based agent in Python that interacts with an environment consisting of rooms in either a dirty or clean state.

The agent perceives the state of its current room and decides whether to clean it or move to another room based on predefined rules. The simulation demonstrates how an intelligent agent makes decisions and interacts with its environment.

## Features

- **Room Environment** – Initializes rooms with user-defined states: Dirty or Clean.
- **Rule-Based Decisions** – Uses predefined rules to determine the agent's actions.
- **Cleaning Mechanism** – Cleans the current room if it is dirty.
- **Room Navigation** – Moves the agent between rooms when the current room is clean.
- **Simulation Steps** – Allows the user to specify how many steps the agent will execute.
- **Environment Updates** – Displays the agent's location, action, and room states after each step.
- **Three-Room Bonus Task** – Extends the environment to three rooms and allows the agent to randomly select a dirty room to visit. Displays the environment using a text-based grid.

## Files

- `TA2_Millares.pdf` – Technical assessment report containing the background, Python source code, laboratory tasks, simulation instructions, and answers to the analysis questions.
- `rule_based_agent.py` – Python script implementing the basic two-room rule-based agent. *(Replace with your actual Python filename if different.)*
- `rule_based_agent_bonus.py` – Python script implementing the optional three-room bonus task. *(Include this file only if you saved the bonus implementation separately.)*

## Technologies Used

- Python 3.x
- Python standard library
  - `random` (used in the bonus task)

## How to Run

1. Install Python 3.x on your computer.
2. Clone or download this repository.
3. Open a terminal in the project directory.
4. Run the basic two-room simulation:

   ```bash
   python rule_based_agent.py
   ```

5. Enter the initial state of rooms A and B when prompted. Use `Dirty` or `Clean`.
6. Enter the number of steps the agent should run.
7. Observe the agent's location, actions, and the updated environment state after each step.

### Running the Bonus Task

If you have the optional three-room implementation, run:

```bash
python rule_based_agent_bonus.py
```

Enter the initial state of rooms A, B, and C, followed by the number of simulation steps. The agent cleans dirty rooms, randomly selects a dirty room when its current room is clean, and remains idle when all rooms are clean.

## Agent Rules

The basic two-room agent follows these rules:

1. If the current room is dirty, clean it.
2. If the current room is clean, move to the other room.

The bonus implementation extends the behavior:

1. If the current room is dirty, clean it without moving.
2. If the current room is clean and other dirty rooms exist, randomly select one and move to it.
3. If all rooms are clean, remain idle.

## Objectives

- Understand the concept of rule-based intelligent agents.
- Implement an agent using Python classes, methods, and conditional statements.
- Allow an agent to perceive its environment and act according to predefined rules.
- Observe and analyze the agent's behavior over multiple simulation steps.
- Explore how the agent can be extended to support additional rooms.

## Author

**Kurt Martin M. Millares**

## Course and Section

- **Course:** CS0065 – Intelligent Systems
- **Section:** BSCSSE – AN42
- **Professor:** Ms. Crisola Tan
- **Assessment:** Technical Assessment 2 (TA2)
- **Date:** October 5, 2026

