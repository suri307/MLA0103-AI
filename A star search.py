graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 2)],
    'C': [('D', 1)],
    'D': []
}

h = {'A': 3, 'B': 2, 'C': 1, 'D': 0}

open_list = [('A', 0)]
visited = []

while open_list:
    open_list.sort(key=lambda x: x[1])
    node, cost = open_list.pop(0)
    visited.append(node)

    if node == 'D':
        print("Goal Reached")
        break

    for n, c in graph[node]:
        f = cost + c + h[n]
        open_list.append((n, f))

print("Path:", " -> ".join(visited))