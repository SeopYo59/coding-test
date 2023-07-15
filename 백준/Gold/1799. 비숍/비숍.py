def check_attack_range(board_ij, pos):
    temp_board_ij = []

    i_pos, j_pos = pos
    for i, j in board_ij:
        if abs(i - i_pos) != abs(j - j_pos):
            temp_board_ij.append((i, j))

    return temp_board_ij


def simul_bishop(board_ij, sum_bishop):
    global max_bishop

    if sum_bishop + len(board_ij) <= max_bishop:
        return

    if not board_ij:
        if max_bishop < sum_bishop:
            max_bishop = sum_bishop
        return

    for idx in range(len(board_ij)):
        i, j = board_ij[idx]
        temp_board_ij = check_attack_range(board_ij[idx + 1:], (i, j))
        simul_bishop(temp_board_ij, sum_bishop + 1)


N = int(input())

board = []
for _ in range(N):
    line = input().split(" ")
    board.append(line)

board_ij_white = []
board_ij_black = []
for i in range(N):
    for j in range(N):
        if board[i][j] == '1':
            if (i + j) % 2 == 0:
                board_ij_white.append((i, j))
            else:
                board_ij_black.append((i, j))

result = 0

max_bishop = 0
simul_bishop(board_ij_white, 0)
result += max_bishop

max_bishop = 0
simul_bishop(board_ij_black, 0)
result += max_bishop

print(result)