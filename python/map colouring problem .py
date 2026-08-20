# Map Coloring Problem using Backtracking

def is_safe(region, color, assignment, graph):
    for neighbor in graph[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True


def map_coloring(regions, colors, graph, assignment):
    # All regions are colored
    if len(assignment) == len(regions):
        return True

    # Select an uncolored region
    for region in regions:
        if region not in assignment:
            break

    # Try each color
    for color in colors:
        if is_safe(region, color, assignment, graph):
            assignment[region] = color

            if map_coloring(regions, colors, graph, assignment):
                return True

            # Backtrack
            del assignment[region]

    return False


# Regions
regions = ["A", "B", "C", "D"]

# Available colors
colors = ["Red", "Green", "Blue"]

# Map connections
graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}

assignment = {}

if map_coloring(regions, colors, graph, assignment):
    print("Map Coloring Solution:")
    for region in regions:
        print(region, "->", assignment[region])
else:
    print("No solution exists.")