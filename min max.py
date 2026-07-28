tree = [3, 5, 2, 9]

def minimax(depth, node, isMax):
    if depth == 2:
        return tree[node]

    if isMax:
        return max(minimax(depth+1, node*2, False),
                   minimax(depth+1, node*2+1, False))
    else:
        return min(minimax(depth+1, node*2, True),
                   minimax(depth+1, node*2+1, True))

print("Optimal Value:", minimax(0, 0, True))