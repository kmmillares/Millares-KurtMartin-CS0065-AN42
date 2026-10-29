# Technical Assessment 4: Knowledge Representation, Rule-Based Reasoning, and Case-Based Reasoning

This repository contains the output for **Technical Assessment 4 (TA4)**
for **CS0065 -- Intelligent Systems**. The project implements a
Python-based Traffic Reasoning System that demonstrates Knowledge
Representation (KR), Rule-Based Reasoning (RBR), and Case-Based
Reasoning (CBR) in a traffic-situation scenario.

The program collects information about the current traffic conditions,
applies predefined IF--THEN rules to recommend actions, and compares the
situation with previously stored cases to retrieve a similar scenario
and its solution. The user can keep or revise the retrieved solution,
after which the new case is retained in the case base.

## Features

-   **Knowledge Base** -- Represents the current traffic situation using
    a Python dictionary.
-   **Interactive User Input** -- Collects the traffic level, rain
    status, accident status, and road-construction status.
-   **Rule-Based Reasoning** -- Applies predefined IF--THEN rules to
    infer traffic-related actions.
-   **Inference Engine** -- Evaluates the stored rules and gathers all
    actions that match the current facts.
-   **Case Base** -- Starts with three past traffic scenarios and their
    recommended solutions.
-   **Similarity Matching** -- Compares the current situation with
    previous cases by counting matching features.
-   **Case Retrieval** -- Selects the past case with the highest
    similarity score.
-   **Solution Reuse** -- Uses the retrieved case's solution as the
    initial recommendation.
-   **Solution Revision** -- Lets the user enter a revised solution or
    press Enter to keep the retrieved one.
-   **Case Retention** -- Adds the current traffic situation and final
    solution to the case base.
-   **Combined Results** -- Displays the actions inferred by RBR and the
    final solution produced by CBR.

## Files

-   `TA4_Millares.pdf` -- Technical assessment report containing the
    background, laboratory tasks, Python implementation, and comparative
    reflection.
-   `traffic_reasoning_system.py` -- Example filename for the Python
    implementation. Replace it with the actual script filename if it
    differs.

## Technologies Used

-   **Python 3.x**
-   **Python standard library**
    -   Dictionaries and lists for facts, rules, and cases
    -   Functions for reasoning and similarity calculations
    -   Console input/output using `input()` and `print()`

No third-party Python packages are required.

## How to Run

1.  Install Python 3.x on your computer.

2.  Clone or download this repository.

3.  Open a terminal in the project directory.

4.  Run the Python script (replace the example filename if needed):

    ``` bash
    python traffic_reasoning_system.py
    ```

5.  Enter the current traffic information when prompted:

    -   Traffic level (`light`, `moderate`, or `heavy`)
    -   Whether it is raining (`yes` or `no`)
    -   Whether there is an accident (`yes` or `no`)
    -   Whether there is road construction (`yes` or `no`)

6.  Review the facts, Rule-Based Reasoning actions, the most similar
    past case, and its similarity score.

7.  When the retrieved solution is displayed, enter a revised solution
    or press Enter to keep it.

8.  Review the final RBR actions, the final CBR solution, and the
    confirmation that the new case was retained.

## Knowledge Representation

The current traffic situation is stored as a dictionary with four
attributes:

-   `traffic_level` -- traffic condition (`light`, `moderate`, or
    `heavy`)
-   `rain` -- whether it is raining (`True` or `False`)
-   `accident` -- whether an accident is present (`True` or `False`)
-   `road_construction` -- whether road construction is present (`True`
    or `False`)

These facts form the knowledge base used by both reasoning approaches.

## Rule-Based Reasoning (RBR)

The system uses IF--THEN functions to infer actions from the traffic
facts:

  -----------------------------------------------------------------------
  Condition                           Inferred action
  ----------------------------------- -----------------------------------
  Traffic level is `heavy`            Take an alternate route.

  It is raining                       Drive carefully because the road is
                                      wet.

  An accident is present              Avoid the area because there is an
                                      accident.

  Road construction is present        Use another road because of road
                                      construction.
  -----------------------------------------------------------------------

The inference engine checks each rule against the current facts and
collects every action whose condition is satisfied. If no rules match,
the program reports that no special action is required.

## Case-Based Reasoning (CBR)

The initial case base contains three example traffic scenarios, each
paired with a recommended solution. The system compares the current
situation with each stored case and counts how many attributes match.

The case with the highest matching score is retrieved, and its solution
is reused as a starting point. The user may revise that solution or keep
it unchanged. The resulting case and final solution are then appended to
the case base.

### CBR Cycle

1.  **Retrieve** -- Find the stored case with the most matching traffic
    features.
2.  **Reuse** -- Retrieve the solution associated with that case.
3.  **Revise** -- Allow the user to modify the solution or keep it as
    provided.
4.  **Retain** -- Add the new traffic situation and final solution to
    the case base.

## Comparing RBR and CBR

-   **RBR** applies fixed, explicitly defined rules to the current
    facts. It is straightforward when conditions and responses can be
    clearly specified.
-   **CBR** uses similarities to previous situations and reuses their
    solutions. It can offer a useful starting point for a new scenario
    when a relevant past case exists, and it allows the user to revise
    the retrieved solution.

The program demonstrates both approaches on the same traffic input so
their outputs can be compared.

## Objectives

-   Construct a knowledge base using Python data structures.
-   Implement Rule-Based Reasoning with IF--THEN rules and an inference
    engine.
-   Implement Case-Based Reasoning with case similarity matching.
-   Retrieve, reuse, revise, and retain cases.
-   Compare how RBR and CBR respond to the same traffic situation.
-   Document observations about knowledge representation and reasoning.

## Limitations

-   The initial CBR case base contains only three predefined traffic
    scenarios.
-   Similarity is calculated by counting matching features; the
    attributes are not weighted differently.
-   The CBR case base is stored in memory while the program runs. The
    provided implementation does not save new cases to a file or
    database, so retained cases are not automatically available in a
    later run.
-   The recommendations are a classroom demonstration and should not
    replace real-time traffic information or official road-safety
    guidance.

## Author

**Kurt Martin Millares**

## Course and Section

-   **Course:** CS0065 -- Intelligent Systems
-   **Section:** BSCSSE -- AN42
-   **Professor:** Ms. Crisola Tan
-   **Assessment:** Technical Assessment 4 (TA4)
-   **Topic:** Knowledge Representation, Rule-Based Reasoning (RBR), and
    Case-Based Reasoning (CBR)
-   **Date:** October 5, 2026
