def clean(N, M, ri, rj, dir, map):
    map[ri][rj] = '-1'
    cnt = 1
    while(True):
        if map[ri][rj] == '0':
            map[ri][rj] = '-1'
            cnt += 1

        if search(ri, rj, N, M, map):
            while(True):
                dir = change_dir(dir)
                if canfront(ri, rj, dir, map):
                    ri, rj = gofront(ri, rj, dir)
                    break
                else:
                    continue

        else:
            ri, rj = goback(ri, rj, dir, map)
            if ri == -1 and rj == -1:
                break

    return cnt

def search(ri, rj, N, M, map):
    if ri-1 >= 0 and map[ri-1][rj] == '0':
        return True
    if ri+1 < N and map[ri+1][rj] == '0':
        return True
    if rj-1 >= 0 and map[ri][rj-1] == '0':
        return True
    if rj+1 < M and map[ri][rj+1] == '0':
        return True

    return False

def goback(ri, rj, dir, map):
    if dir == 0 and ri+1 < N and map[ri+1][rj] != '1':
        return (ri+1, rj)
    if dir == 1 and rj-1 >= 0 and map[ri][rj-1] != '1':
        return (ri, rj-1)
    if dir == 2 and ri-1 >= 0 and map[ri-1][rj] != '1':
        return (ri-1, rj)
    if dir == 3 and rj+1 < M and map[ri][rj+1] != '1':
        return (ri, rj+1)

    return (-1, -1)

def change_dir(dir):
    dir -= 1
    if dir == -1:
        dir = 3
    return dir

def canfront(ri, rj, dir, map):
    if dir == 2 and ri+1 < N and map[ri+1][rj] == '0':
        return True
    if dir == 3 and rj-1 >= 0 and map[ri][rj-1] == '0':
        return True
    if dir == 0 and ri-1 >= 0 and map[ri-1][rj] == '0':
        return True
    if dir == 1 and rj+1 < M and map[ri][rj+1] == '0':
        return True

    return False

def gofront(ri, rj, dir):
    if dir == 2:
        return (ri+1, rj)
    if dir == 3:
        return (ri, rj-1)
    if dir == 0:
        return (ri-1, rj)
    if dir == 1:
        return (ri, rj+1)

N, M = map(int, input().split(" "))
ri, rj, dir = map(int, input().split(" "))
map = []
for i in range(N):
    map.append(input().split(" "))

print(clean(N, M, ri, rj, dir, map))