def vaild(popul, y, x, map):
    global N
    global L
    global R

    if (0 <= y and y < N) and (0 <= x and x < N) and (map[y][x] != 'X'):

        diff_value = abs(popul-map[y][x])
        if L <= diff_value and diff_value <= R:
            return True

    else:
        return False

def BFS(map, queue, united):
    while queue:
        x, y, popul = queue.pop(0)

        if vaild(popul, y+1, x, map):
            queue.append((x, y+1, map[y+1][x]))
            united.append((x, y+1, map[y+1][x]))
            map[y+1][x] = 'X'

        if vaild(popul, y-1, x, map):
            queue.append((x, y-1, map[y-1][x]))
            united.append((x, y-1, map[y-1][x]))
            map[y-1][x] = 'X'

        if vaild(popul, y, x+1, map):
            queue.append((x+1, y, map[y][x+1]))
            united.append((x+1, y, map[y][x+1]))
            map[y][x+1] = 'X'

        if vaild(popul, y, x-1, map):
            queue.append((x-1, y, map[y][x-1]))
            united.append((x-1, y, map[y][x-1]))
            map[y][x-1] = 'X'

def cal(united_list, map):
    for united in united_list:
        sum = 0
        for i in range(len(united)):
            sum += united[i][2]

        value = int(sum/len(united))

        for i in range(len(united)):
            x = united[i][0]
            y = united[i][1]
            map[y][x] = value

global N
global L
global R

N, L, R = map(int, input().split(" "))

MAP = []
for i in range(N):
    MAP.append(list(map(int, input().split(" "))))


cnt = 0
while True:
    united_list = []
    for i in range(N):
        for j in range(N):
            if MAP[i][j] != 'X':
                queue = [(j, i, MAP[i][j])]
                united = [(j, i, MAP[i][j])]
                MAP[i][j] = 'X'
                BFS(MAP, queue, united)

                if len(united) > 1:
                    united_list.append(united)
                else:
                    MAP[i][j] = united[0][2]

    if not united_list:
        break

    while united_list:
        cal(united_list, MAP)
        united_list.pop(0)

    cnt += 1

print(cnt)