graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

h = {
    'A': 6,
    'B': 4,
    'C': 3,
    'D': 5,
    'E': 2,
    'F': 1,
    'G': 0
}

open_list = ['A']
visited = []

while open_list:
    open_list.sort(key=lambda x: h[x])
    node = open_list.pop(0)

    if node not in visited:
        visited.append(node)

        if node == 'G':
            print("Goal Reached")
            break

        open_list.extend(graph[node])

print("Path:", " -> ".join(visited))