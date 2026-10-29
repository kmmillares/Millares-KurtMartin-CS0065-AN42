# Technical Assessment 3: Case-Based Reasoning (CBR) System Development

This repository contains the output for Technical Assessment 3 (TA3) for
**CS0065 -- Intelligent Systems**. The project implements a Case-Based
Reasoning (CBR) system in Python using an **Intelligent Tutoring System
(ITS)** scenario.

The program helps identify a student's mathematics learning difficulties
by comparing a new student case with previously stored cases. It ranks
past cases using a weighted similarity score, retrieves the most
relevant case, generates personalized feedback and learning
interventions based on the student's reported errors, and retains the
new case in the case base.

## Features

-   **Initial Case Base** -- Starts with five past student cases
    containing a mathematics topic, error patterns, difficulty level,
    score, and a corresponding solution.
-   **Dynamic User Input** -- Prompts the user to enter a new student's
    topic, difficulty, score, and error patterns.
-   **Input Validation** -- Checks the difficulty selection, keeps the
    score within 0--100, and validates the selected error-pattern
    numbers.
-   **Weighted Similarity Assessment** -- Compares the new case with
    stored cases using topic, error patterns, difficulty, and score.
-   **Similarity Ranking** -- Displays the stored cases ranked from
    highest to lowest similarity.
-   **Case Retrieval** -- Identifies the most relevant past case for the
    new student problem.
-   **Personalized Solution Adaptation** -- Generates feedback, lesson
    suggestions, and interventions based on the student's selected
    errors.
-   **Learning and Retention** -- Adds the new case and its adapted
    solution to the in-memory case base.
-   **Updated Case Base** -- Displays the cases after the new case has
    been added.

## Files

-   `TA3_Millares.pdf` -- Technical assessment report containing the
    background, instructions, Python implementation, documentation, and
    pair reflection.
-   `intelligent_tutoring_system.py` -- Python implementation of the
    CBR-based Intelligent Tutoring System. Use the actual Python
    filename from your project if it differs from this example.

## Technologies Used

-   **Python 3.x**
-   **Python standard library**
    -   `set` operations for comparing error patterns
    -   `input()` and `print()` for console interaction
    -   `round()` and built-in functions for similarity calculations and
        result handling

The program does not require third-party Python packages.

## How to Run

1.  Install Python 3.x on your computer.

2.  Clone or download the repository.

3.  Open a terminal in the project directory.

4.  Run the Python script (replace the example filename if your script
    has a different name):

    ``` bash
    python intelligent_tutoring_system.py
    ```

5.  Enter the requested student information:

    -   Mathematics topic
    -   Difficulty (`easy`, `medium`, or `hard`)
    -   Student score from `0` to `100`
    -   Error-pattern numbers selected from the displayed list

6.  Review the similarity ranking, the most relevant past case, the
    personalized feedback and lessons, and the recommended intervention.

7.  Review the confirmation that the new case was saved and the updated
    case base.

### Available Error Patterns

The program lists these error patterns for selection:

1.  Wrong formula
2.  Sign error
3.  Substitution error
4.  Arithmetic error
5.  Transposition error
6.  Discriminant error

Enter the corresponding numbers separated by commas, following the
example shown by the program.

## Case-Based Reasoning Process

The system follows the main stages of the CBR cycle:

1.  **Retrieve** -- Compare the new student's problem with the cases
    already stored in the case base and rank them by similarity.
2.  **Reuse** -- Use the most relevant past case as a reference for the
    new problem.
3.  **Revise** -- Adapt feedback, lesson suggestions, and interventions
    to address the error patterns selected for the current student.
4.  **Retain** -- Save the new student case together with its adapted
    solution in the case base and display the updated list.

## Similarity Assessment

The program calculates a similarity score out of 100 using four
attributes:

  ------------------------------------------------------------------------
  Attribute                                   Weight How it is compared
  --------------------- ---------------------------- ---------------------
  Mathematics topic                              40% Adds 40 points when
                                                     the topics match.

  Error patterns                                 40% Uses the Jaccard
                                                     similarity of the two
                                                     sets of error
                                                     patterns, multiplied
                                                     by 40.

  Difficulty                                     10% Adds 10 points when
                                                     the difficulty levels
                                                     match.

  Student score                                  10% Calculates score
                                                     similarity from the
                                                     absolute difference
                                                     between the two
                                                     scores, then
                                                     multiplies it by 10.
  ------------------------------------------------------------------------

The program sorts the cases by similarity in descending order. The case
with the highest similarity score is selected as the most relevant past
case.

## Solution Adaptation

The system creates a response based on the new student's selected error
patterns. Depending on the errors, it can recommend feedback and lessons
such as:

-   Reviewing the correct formula
-   Checking positive and negative signs
-   Identifying coefficients before substitution
-   Rechecking arithmetic
-   Practicing transposition rules
-   Reviewing and calculating the discriminant

It also includes an intervention reference to the retrieved case. The
generated feedback, lessons, and interventions are stored as the
solution for the new case.

## Case Retention and Data Storage

After the solution is generated, the program adds the new case to the
case base and displays a confirmation and the updated number of cases.

**Note:** The case base is stored in the program's memory while it runs.
The provided implementation does not write cases to a file or database,
so newly added cases are not automatically preserved after the program
exits.

## Objectives

-   Understand and apply the Case-Based Reasoning cycle: retrieval,
    reuse, revision, and retention.
-   Represent previous student problems and solutions using Python data
    structures.
-   Compare student cases using a weighted similarity method.
-   Retrieve a relevant past case to support a new problem.
-   Adapt feedback, lessons, and interventions to a student's reported
    mathematics errors.
-   Demonstrate learning by adding the newly solved case to the case
    base.
-   Explore how experiential knowledge can support personalized
    learning.

## Limitations

-   The system uses five predefined cases as its initial case base, so
    the quality of retrieval depends on how well those cases represent a
    new student's problem.
-   The available error patterns and adaptation rules are predefined.
-   The program adds new cases only to its in-memory case base during
    the current run; it does not persist them between separate runs.
-   The system provides educational guidance and is a classroom
    demonstration, not a replacement for a teacher's assessment.

## Authors

-   **Kurt Millares**
-   **Tyrael Lance Peralta**

## Course and Section

-   **Course:** CS0065 -- Intelligent Systems
-   **Section:** BSCSSE -- AN42
-   **Professor:** Ms. Crisola Tan
-   **Assessment:** Technical Assessment 3 (TA3)
-   **Topic:** Case-Based Reasoning (CBR) System Development
-   **Case Study:** Intelligent Tutoring System
-   **Date:** October 5, 2026
