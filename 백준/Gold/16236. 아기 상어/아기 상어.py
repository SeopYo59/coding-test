def Vaild(shark_x, shark_y, shark_size):
    global N
    global space
    if (0 <= shark_x < N) and (0 <= shark_y < N) and (check_step[shark_y][shark_x] != 1):
        if shark_size < space[shark_y][shark_x]:
            return False
        return True
    else:
        return False

def Bfs(queue, shark_size):
    edible = []
    min_dis = 0
    dx = [0, -1, 1, 0]
    dy = [-1, 0, 0, 1]
    while queue:
        shark_x, shark_y = queue.pop(0)

        if 1 <= space[shark_y][shark_x] <= 6 :
            if shark_size > space[shark_y][shark_x]:
                if min_dis == 0:
                    min_dis = check_dis[shark_y][shark_x]
                else:
                    if min_dis != check_dis[shark_y][shark_x]:
                        return ((sorted(edible, key=lambda x: (x[1], x[0])))[0], min_dis)
                edible.append((shark_x, shark_y))

        for i in range(4):
            nx = shark_x+dx[i]
            ny = shark_y+dy[i]
            if Vaild(nx, ny, shark_size):
                queue.append( (nx, ny) )
                check_step[ny][nx] = 1
                current_dis = check_dis[shark_y][shark_x]+1
                check_dis[ny][nx] = current_dis

    if edible:
        return ( (sorted(edible, key=lambda x: (x[0], x[1])))[0], min_dis )

    return False

N = int(input())
space = []

for i in range(N):
    space.append(list(map(int, input().split(" "))))
    if 9 in space[i]:
        shark_x = space[i].index(9)
        shark_y = i

shark_size = 2
eat = 0
time = 0

while True:
    check_dis = [ [0 for _ in range(N)] for _ in range(N)]
    check_step = [ [0 for _ in range(N)] for _ in range(N)]

    queue = [(shark_x, shark_y)]
    check_step[shark_y][shark_x] = 1

    next = Bfs(queue, shark_size)

    if not next:
        break
    else:
        space[shark_y][shark_x] = 0
        shark_x, shark_y = next[0]
        dis = next[1]

        time += dis

        eat += 1
        if eat == shark_size:
            eat = 0
            shark_size += 1

        space[shark_y][shark_x] = 0

print(time)