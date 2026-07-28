from heapq import *

g = {
    'P': [('Q', 2), ('R', 4)],
    'Q': [('S', 3)],
    'R': [('T', 1)],
    'S': [],
    'T': []
}

pq = [(0, 'P')]
v = set()

while pq:
    c, n = heappop(pq)
    if n not in v:
        print(n, c)
        v.add(n)
        for x, w in g[n]:
            heappush(pq, (c + w, x))