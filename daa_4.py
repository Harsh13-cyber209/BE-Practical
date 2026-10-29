
def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False

        for j in range(n):
            if board[i][j] == 1 and abs(i-row) == abs(j-col):
                return False

    return True


def solve(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            if solve(board, row+1, n):
                return True

            board[row][col] = 0  

    return False


n = 4
board = [[0]*n for i in range(n)]

# First queen fixed at row 0, column 1
board[0][1] = 1

if solve(board, 1, n):
    for row in board:
        print(row)
else:
    print("No solution")
