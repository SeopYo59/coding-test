def cal(map, N):
    max = 0
    for i in range(N):
        for j in range(N):
            len = 1
            c = 1
            while True:
                if (0 <= i-c and i-c <N) and (map[i-c][j] == map[i][j]):
                    len += 1
                    c += 1
                else: break

            c = 1
            while True:
                if (0 <= i+c and i+c <N) and (map[i+c][j] == map[i][j]):
                    len += 1
                    c += 1
                else: break

            if max < len:
                max = len

            len = 1
            c = 1
            while True:
                if (0 <= j - c and j - c < N) and (map[i][j - c] == map[i][j]):
                    len += 1
                    c += 1
                else:
                    break

            c = 1
            while True:
                if (0 <= j + c and j + c < N) and (map[i][j + c] == map[i][j]):
                    len += 1
                    c += 1
                else:
                    break

            if max < len:
                max = len


    return max


N = int(input())
map = []
for i in range(N):
    map.append(list(input()))

max = 0
for i in range(N):
    for j in range(N):
        if (0 <= i-1 and i-1 < N) and (map[i][j] != map[i-1][j]):
            map[i][j], map[i-1][j] = map[i-1][j], map[i][j]
            m = cal(map, N)
            map[i][j], map[i - 1][j] = map[i - 1][j], map[i][j]
            if max < m: max = m

        if (0 <= i+1 and i+1 < N) and (map[i][j] != map[i+1][j]):
            map[i][j], map[i+1][j] = map[i+1][j], map[i][j]
            m = cal(map, N)
            map[i][j], map[i + 1][j] = map[i + 1][j], map[i][j]
            if max < m: max = m

        if (0 <= j-1 and j-1 < N) and (map[i][j-1] != map[i][j-1]):
            map[i][j], map[i][j-1] = map[i][j-1], map[i][j]
            m = cal(map, N)
            map[i][j], map[i][j-1] = map[i][j-1], map[i][j]
            if max < m: max = m

        if (0 <= j+1 and j+1 < N) and (map[i][j] != map[i][j+1]):
            map[i][j], map[i][j+1] = map[i][j+1], map[i][j]
            m = cal(map, N)
            map[i][j], map[i][j+1] = map[i][j+1], map[i][j]
            if max < m: max = m

print(max)