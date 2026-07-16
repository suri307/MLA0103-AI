from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque()
    queue.append(start)
    visited.add(start)
    print("BFS Traversal:")

    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


graph = {
    '1': ['2', '7'],
    '2': ['3', '6'],
    '3': ['4','5'],
    '4': [],
    '5': [],
    '6': [],
    '7': ['8','10'],
    '8': ['9'],
    '9': [],
    '10':[]
}

start= '1'
bfs(graph, start)
