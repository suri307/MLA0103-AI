# Forward Chaining

# Initial facts
facts = {
    "A",
    "B"
}

# Rules
# If conditions are true -> conclusion
rules = [
    (["A"], "C"),
    (["B"], "D"),
    (["C", "D"], "E"),
    (["E"], "F")
]


def forward_chaining(facts, rules):

    facts = set(facts)
    changed = True

    while changed:
        changed = False

        for conditions, conclusion in rules:

            # Check whether all conditions are satisfied
            if all(condition in facts for condition in conditions):

                # Add new conclusion
                if conclusion not in facts:
                    facts.add(conclusion)
                    changed = True

                    print(
                        "Derived:",
                        conclusion
                    )

    return facts


# Run Forward Chaining
result = forward_chaining(facts, rules)

print("\nFinal Facts:")
print(result)