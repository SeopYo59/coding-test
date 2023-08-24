def valid(y, x, map):
    if (0 <= y and y < n) and (0 <= x and x < m):
        if map[y][x] == "1":
            return True

def bfs(queue, map, dmap):
    des = 0
    cnt = 1
    cnt2 = 0
    while(queue):
        if cnt == 0:
            cnt = cnt2
            cnt2 = 0

        y, x = queue.pop(0)
        dmap[y][x] = des


        cnt -= 1
        if cnt == 0:
            des += 1


        if valid(y+1, x, map):
            queue.append((y+1, x))
            map[y+1][x] = "X"
            cnt2 += 1
        if valid(y-1, x, map):
            queue.append((y-1, x))
            map[y-1][x] = "X"
            cnt2 += 1
        if valid(y, x+1, map):
            queue.append((y, x+1))
            map[y][x+1] = "X"
            cnt2 += 1
        if valid(y, x-1, map):
            queue.append((y, x-1))
            map[y][x-1] = "X"
            cnt2 += 1

n, m = map(int, input().split(" "))
map = []
dmap = []

for i in range(n):
    map.append(list(input().split(" ")))
    dmap.append([0 for j in range(m)])
    if "2" in map[i]:
        goal = (i, map[i].index("2"))

queue = [goal]
bfs(queue, map, dmap)

for i in range(n):
    for j in range(m):
        if map[i][j] == "1":
            dmap[i][j] = -1

for i in range(n):
    for j in range(m):
        print(dmap[i][j] , end = " ")
    print("")