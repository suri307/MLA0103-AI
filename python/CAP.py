from itertools import permutations

def solve_cryptarithmetic():
    # Letters in SEND + MORE = MONEY
    letters = "SENDMORY"

    # Leading letters cannot be zero
    leading = {"S", "M"}

    for values in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, values))

        # Leading letters cannot be 0
        if any(mapping[ch] == 0 for ch in leading):
            continue

        # Convert words to numbers
        SEND = (
            mapping["S"] * 1000 +
            mapping["E"] * 100 +
            mapping["N"] * 10 +
            mapping["D"]
        )

        MORE = (
            mapping["M"] * 1000 +
            mapping["O"] * 100 +
            mapping["R"] * 10 +
            mapping["E"]
        )

        MONEY = (
            mapping["M"] * 10000 +
            mapping["O"] * 1000 +
            mapping["N"] * 100 +
            mapping["E"] * 10 +
            mapping["Y"]
        )

        # Check the constraint
        if SEND + MORE == MONEY:
            print("Solution found:")
            for letter in sorted(mapping):
                print(letter, "=", mapping[letter])

            print("\nSEND =", SEND)
            print("MORE =", MORE)
            print("MONEY =", MONEY)
            print("\n", SEND, "+", MORE, "=", MONEY)
            return

    print("No solution found.")


solve_cryptarithmetic()