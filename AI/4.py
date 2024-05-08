"""
4.Implement a solution for a Constraint Satisfaction Problem using Branch and Bound and Backtracking
for n-queens problem or a graph coloring problem.
"""
def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True
def solve_nq_util(board, col):
    if col >= len(board):
        return True
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_nq_util(board, col + 1):
                return True
            board[i][col] = 0
    return False
def solve_n_queens(n):
    board = [[0]*n for _ in range(n)]
    if not solve_nq_util(board, 0):
        return None
    return board
def print_solution(board):
    for row in board:
        print(" ".join("Q" if x else "." for x in row))
print("Enter the size of board n*n")
n=int(input())
solution = solve_n_queens(n)
if solution:
    print("One of the solutions for the", n, "Queens problem:")
    print_solution(solution)
else:
    print("No solution exists.")