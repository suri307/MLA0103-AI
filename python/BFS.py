from collections import deque
g = {
    'P': ['Q', 'R'],
    'Q': ['S'],
    'R': ['T'],
    'S': [],
    'T': []
}
q = deque(['P'])
v = set()
while q:
    n = q.popleft()
    if n not in v:
        print(n, end=" ")
        v.add(n)
        q.extend(g[n])