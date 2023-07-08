from collections import deque

# 1. 맵 정보 입력받기
def printMap(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            print(f"{map[i][j]} ", end='')
        print("")
    print("")
    print("")

def vaild(x, y):
    if y < 0 or N <= y:
        return 0
    if x < 0 or M <= x:
        return 0
    if map[y][x] == '0' or map[y][x] == 'X':
        return 0
    if map[y][x] == 'V':
        return 0


    return 1

def getLocation(x, y):
    location = {}
    location['x'] = x
    location['y'] = y
    return location


N, M = map(int, input().split())

map = []
for i in range(N):
    map.append( list(input()) )

#printMap(map)

# 2.BFS
queue1 = deque()
queue1.append(getLocation(0, 0))
queue2 = deque()

distance = 0
while True:
    while queue1:
        here = queue1.popleft()
        x = here['x']
        y = here['y']
        #print(f'({x}, {y})')
        if(x == M-1 and y == N-1):
            print(distance+1)
            exit(0)

        map[y][x] = 'X'
        #printMap(map)
        if vaild(x + 1, y):
            queue2.append(getLocation(x + 1, y))
            map[y][x + 1] = 'V'
        if vaild(x, y + 1):
            queue2.append(getLocation(x, y + 1))
            map[y + 1][x] = 'V'
        if vaild(x - 1, y):
            queue2.append(getLocation(x - 1, y))
            map[y][x - 1] = 'V'
        if vaild(x, y - 1):
            queue2.append(getLocation(x, y - 1))
            map[y - 1][x] = 'V'

    if not queue1 and not queue2:
        print("목적지로 못간다.")
        exit(1)
    else:
        distance += 1

    #print(queue1, queue2)

    while queue2:
        here = queue2.popleft()
        x = here['x']
        y = here['y']
        #print(f'({x}, {y})')
        if(x == M-1 and y == N-1):
            print(distance+1)
            exit(0)

        map[y][x] = 'X'
        #printMap(map)
        if vaild(x + 1, y):
            queue1.append(getLocation(x + 1, y))
            map[y][x + 1] = 'V'
        if vaild(x, y + 1):
            queue1.append(getLocation(x, y + 1))
            map[y + 1][x] = 'V'
        if vaild(x - 1, y):
            queue1.append(getLocation(x - 1, y))
            map[y][x - 1] = 'V'
        if vaild(x, y - 1):
            queue1.append(getLocation(x, y - 1))
            map[y - 1][x] = 'V'

    if not queue1 and not queue2:
        print("목적지로 못간다.")
        exit(1)
    else:
        distance += 1

    #print(queue1, queue2)