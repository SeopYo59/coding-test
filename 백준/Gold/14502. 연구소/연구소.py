import copy

N, M = map(int, input().split(" "))
map = []
for i in range(N):
    map.append(list(input().split(" ")))
def dfs(N, M, map, wall):
    global max

    if wall == 3:
        safe = virus_simul(N, M, map)

        if max < safe:
            max = safe
        return

    for i in range(N):
        for j in range(M):
            if map[i][j] == '0':
                temp = copy.deepcopy(map)
                temp[i][j] = '1'
                dfs(N, M, temp, wall+1)

def virus_simul(N, M, map):
    temp = copy.deepcopy(map)

    for i in range(N):
        for j in range(M):
            if temp[i][j] == '2':
                spread(i, j, N, M, temp)

    safe = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == '0':
                safe += 1

    return safe

def spread(y, x, N, M, map):
    map[y][x] = '2'

    if y+1 < N and map[y+1][x] == '0':
        spread(y+1, x, N, M, map)
    if y-1 >= 0 and map[y-1][x] == '0':
        spread(y-1, x, N, M, map)
    if x+1 < M and map[y][x+1] == '0':
        spread(y, x+1, N, M, map)
    if x-1 >= 0 and map[y][x-1] == '0':
        spread(y, x-1, N, M, map)

    return

def pmap(map):
    for hang in map:
        print(hang)
    print(" ")

max = 0
dfs(N, M, map, 0)
print(max)