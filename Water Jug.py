from collections import deque

def water_jug():
    visited = set()
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue
        visited.add((x, y))

        print((x, y))

        if x == 2 or y == 2:
            print("Goal Reached!")
            return

        next_states = [
            (4, y),                    # Fill Jug1
            (x, 3),                    # Fill Jug2
            (0, y),                    # Empty Jug1
            (x, 0),                    # Empty Jug2
            (max(0, x-(3-y)), min(3, y+x)),  # Pour Jug1 -> Jug2
            (min(4, x+y), max(0, y-(4-x)))   # Pour Jug2 -> Jug1
        ]

        for state in next_states:
            if state not in visited:
                queue.append(state)

water_jug()