# N-Queen Problem using Backtracking

def is_safe(board, row, col, n):
    # Check the same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i] == j:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queen(board, row, n):
    # All queens are placed
    if row == n:
        return True

    # Try each column
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col

            if solve_n_queen(board, row + 1, n):
                return True

            # Backtrack
            board[row] = -1

    return False


def print_board(board, n):
    for row in range(n):
        for col in range(n):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# Main program
n = int(input("Enter the value of N: "))

board = [-1] * n

if solve_n_queen(board, 0, n):
    print("\nSolution:")
    print_board(board, n)
else:
    print("No solution exists.")