# Backward Chaining

# Initial facts
facts = {
    "A",
    "B"
}

# Rules
# conditions -> conclusion
rules = [
    (["A"], "C"),
    (["B"], "D"),
    (["C", "D"], "E"),
    (["E"], "F")
]


def backward_chaining(goal, facts, rules, visited=None):

    if visited is None:
        visited = set()

    # Goal is already a known fact
    if goal in facts:
        return True

    # Avoid infinite loops
    if goal in visited:
        return False

    visited.add(goal)

    # Find rules that can produce the goal
    for conditions, conclusion in rules:

        if conclusion == goal:

            # Prove all conditions
            if all(
                backward_chaining(
                    condition,
                    facts,
                    rules,
                    visited.copy()
                )
                for condition in conditions
            ):
                return True

    return False


# Goal to prove
goal = "F"

# Check the goal
if backward_chaining(goal, facts, rules):
    print("Goal:", goal)
    print("Goal can be proved.")
else:
    print("Goal:", goal)
    print("Goal cannot be proved.")