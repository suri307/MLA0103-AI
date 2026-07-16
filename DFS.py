g = {
    'P': ['Q', 'R'],
    'Q': ['S'],
    'R': ['T'],
    'S': [],
    'T': []
}

v = set()

def dfs(n):
    if n not in v:
        print(n, end=" ")
        v.add(n)
        for i in g[n]:
            dfs(i)

dfs('P')