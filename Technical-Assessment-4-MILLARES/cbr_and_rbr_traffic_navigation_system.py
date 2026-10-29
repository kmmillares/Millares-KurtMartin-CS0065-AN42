# ============================================
# PART 1 — KNOWLEDGE REPRESENTATION
# ============================================

# Facts will be filled in by the user
facts = {}


# ============================================
# PART 2 — RULE-BASED REASONING
# ============================================

# Task 2A — IF-THEN Rules

def rule_heavy_traffic(facts):
    if facts["traffic_level"] == "heavy":
        return "Take an alternate route"


def rule_rain(facts):
    if facts["rain"]:
        return "Drive carefully because the road is wet"


def rule_accident(facts):
    if facts["accident"]:
        return "Avoid the area because there is an accident"


def rule_construction(facts):
    if facts["road_construction"]:
        return "Use another road because of road construction"


# Store all rules
rules = [
    rule_heavy_traffic,
    rule_rain,
    rule_accident,
    rule_construction
]


# ============================================
# Task 2B — INFERENCE ENGINE
# ============================================

def inference_engine(facts, rules):

    actions = []

    for rule in rules:

        result = rule(facts)

        if result is not None:
            actions.append(result)

    return actions


# ============================================
# PART 3 — CASE-BASED REASONING
# ============================================

# Task 3A — Case Base

case_base = [

    {
        "problem": {
            "traffic_level": "heavy",
            "rain": False,
            "accident": True,
            "road_construction": False
        },
        "solution": "Take an alternate route to avoid the accident."
    },

    {
        "problem": {
            "traffic_level": "moderate",
            "rain": True,
            "accident": False,
            "road_construction": False
        },
        "solution": "Drive slowly and carefully because the road is wet."
    },

    {
        "problem": {
            "traffic_level": "heavy",
            "rain": True,
            "accident": False,
            "road_construction": True
        },
        "solution": "Use another road because of heavy traffic and construction."
    }
]


# ============================================
# CBR — RETRIEVE
# ============================================

def similarity(current_problem, past_problem):

    score = 0

    for feature in current_problem:

        if current_problem[feature] == past_problem[feature]:
            score += 1

    return score


def retrieve(current_problem, case_base):

    best_case = None
    best_score = -1

    for case in case_base:

        score = similarity(
            current_problem,
            case["problem"]
        )

        if score > best_score:

            best_score = score
            best_case = case

    return best_case, best_score


# ============================================
# CBR — REUSE
# ============================================

def reuse(retrieved_case):

    if retrieved_case is not None:
        return retrieved_case["solution"]

    return "No similar case found."


# ============================================
# CBR — REVISE
# ============================================

def revise(solution):

    print("\nRetrieved Solution:")
    print(solution)

    new_solution = input(
        "\nEnter a new solution "
        "(or press Enter to keep the retrieved solution): "
    )

    if new_solution.strip() == "":
        return solution

    return new_solution


# ============================================
# CBR — RETAIN
# ============================================

def retain(case_base, problem, solution):

    new_case = {
        "problem": problem,
        "solution": solution
    }

    case_base.append(new_case)


# ============================================
# USER INPUT
# ============================================

print("===================================")
print("TRAFFIC REASONING SYSTEM")
print("===================================")

print("\nPlease enter the current traffic situation.\n")


# Get traffic information from the user

traffic_level = input(
    "Traffic level (light/moderate/heavy): "
).lower()

rain_input = input(
    "Is it raining? (yes/no): "
).lower()

accident_input = input(
    "Is there an accident? (yes/no): "
).lower()

construction_input = input(
    "Is there road construction? (yes/no): "
).lower()


# Convert yes/no answers to True or False

rain = rain_input == "yes"
accident = accident_input == "yes"
road_construction = construction_input == "yes"


# Create the Knowledge Base using user input

facts = {
    "traffic_level": traffic_level,
    "rain": rain,
    "accident": accident,
    "road_construction": road_construction
}


# ============================================
# PART 2C — RUN RULE-BASED REASONING
# ============================================

print("\n===================================")
print("RULE-BASED REASONING")
print("===================================")

print("\nCurrent Traffic Facts:")
print(facts)


# Run inference engine AFTER user input

actions = inference_engine(facts, rules)


print("\nRule-Based Reasoning Actions:")

if len(actions) == 0:

    print("- No special action is required.")

else:

    for action in actions:
        print("- " + action)


# ============================================
# PART 3 — RUN CASE-BASED REASONING
# ============================================

print("\n===================================")
print("CASE-BASED REASONING")
print("===================================")


# The same user input is used as the current CBR problem

current_problem = facts


# RETRIEVE

retrieved_case, score = retrieve(
    current_problem,
    case_base
)


print("\nMost Similar Past Case:")
print(retrieved_case["problem"])

print("\nSimilarity Score:", score)


# REUSE

solution = reuse(retrieved_case)


# REVISE

final_solution = revise(solution)


# RETAIN

retain(
    case_base,
    current_problem,
    final_solution
)


# ============================================
# FINAL RESULT
# ============================================

print("\n===================================")
print("FINAL RESULT")
print("===================================")

print("\nRule-Based Actions:")

if len(actions) == 0:

    print("- No special action is required.")

else:

    for action in actions:
        print("- " + action)


print("\nCase-Based Solution:")
print("- " + final_solution)

print("\nNew case has been retained successfully.")