def roll(dice, dir):
    if dir == "1":
        dice[1].append(dice[0][0])
        dice[0][0] = dice[1].pop(0)

    elif dir == "2":
        dice[1].insert(0, dice[0][0])
        dice[0][0] = dice[1].pop()

    elif dir == "3":
        dice[0].insert(1, dice[0][0])
        dice[1].insert(1, dice[0].pop(2))
        dice[2].insert(1, dice[1].pop(2))
        dice[0][0] = dice[2].pop(2)

    elif dir == "4":
        dice[2].insert(1, dice[0][0])
        dice[1].insert(1, dice[2].pop(2))
        dice[0].insert(1, dice[1].pop(2))
        dice[0][0] = dice[0].pop(2)

def valid(y, x, N, M):
    if (0 <= y and y < N) and (0 <= x and x < M):
        return True

    else:
        return False

N, M, y, x, K = map(int, input().split(" "))

map = []
for i in range(N):
    map.append(input().split(" "))

dice = [[0, 0, 0] for i in range(3)]

cmd = list(input().split())

while cmd:

    dir = cmd.pop(0)

    if dir == "1" and valid(y, x+1, N, M):
        x += 1
    elif dir == "2" and valid(y, x-1, N, M):
        x -= 1
    elif dir == "3" and valid(y-1, x, N, M):
        y -= 1
    elif dir == "4" and valid(y+1, x, N, M):
        y += 1
    else:
        continue

    roll(dice, dir)

    if map[y][x] == "0":
        map[y][x] = str(dice[1][1])

    else:
        dice[1][1] = str(map[y][x])
        map[y][x] = "0"

    print(dice[0][0])