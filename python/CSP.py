# Constraint Satisfaction Problem (CSP)
# Map Coloring using Backtracking

def is_safe(region, color, assignment, neighbors):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True


def solve_csp(regions, colors, neighbors, assignment):
    # If all regions are assigned
    if len(assignment) == len(regions):
        return True

    # Select an unassigned region
    for region in regions:
        if region not in assignment:
            break

    # Try each color
    for color in colors:
        if is_safe(region, color, assignment, neighbors):
            assignment[region] = color

            if solve_csp(regions, colors, neighbors, assignment):
                return True

            # Backtrack
            del assignment[region]

    return False


# Variables
regions = ["A", "B", "C", "D"]

# Available colors
colors = ["Red", "Green", "Blue"]

# Constraints: neighboring regions must have different colors
neighbors = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}

# Store solution
assignment = {}

# Solve CSP
if solve_csp(regions, colors, neighbors, assignment):
    print("CSP Solution:")
    for region in regions:
        print(region, "->", assignment[region])
else:
    print("No solution exists.")