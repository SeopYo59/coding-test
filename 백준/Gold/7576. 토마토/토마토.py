def canInfection(x, y):
    if y < 0 or N <= y:
        return 0
    if x < 0 or M <= x:
        return 0

    if box[y][x] == '0':
        return 1
    else:
        return 0

# 1. 입력
M, N = map(int, input().split())

box = []
for i in range(N):
    box.append(input().split(" "))

# 2. 토마토 상태 변화 구현
days = 0
expected = []
for i in range(N):
    for j in range(M):
        if box[i][j] == '1':
            expected.append( (j, i) )
ripe = []

while expected:
    ripe.clear()
    ripe = expected.copy()
    expected.clear()

    while ripe:
        ripeTomato = ripe.pop()
        x = int(ripeTomato[0])
        y = int(ripeTomato[1])

        if canInfection(x+1, y):
            box[y][x+1] = 'V'
            expected.append( (x+1, y) )
        if canInfection(x-1, y):
            box[y][x-1] = 'V'
            expected.append( (x-1, y) )
        if canInfection(x, y+1):
            box[y+1][x] = 'V'
            expected.append( (x, y+1) )
        if canInfection(x, y-1):
            box[y-1][x] = 'V'
            expected.append( (x, y-1) )

    days += 1

# 3. 출력
for sublist in box:
    if '0' in sublist:
        print(-1)
        exit(0)

print(days - 1)