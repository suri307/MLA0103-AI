tree = [3, 5, 6, 9]

def alphabeta(depth, node, alpha, beta, isMax):
    if depth == 2:
        return tree[node]

    if isMax:
        value = -999
        for i in range(2):
            value = max(value, alphabeta(depth+1, node*2+i, alpha, beta, False))
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value
    else:
        value = 999
        for i in range(2):
            value = min(value, alphabeta(depth+1, node*2+i, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value

print("Optimal Value:", alphabeta(0, 0, -999, 999, True))