def dfs(house, chicken, M, choice):
    global min

    if len(choice) == M:
        total_dis = cal(house, choice)

        if min == -1:
            min = total_dis
        elif total_dis < min:
            min = total_dis
        return

    for i in range(len(chicken)):
        temp = choice.copy()
        temp.append(chicken[i])
        dfs(house, chicken[i+1:], M, temp)

def cal(house, chicken):
    total_dis = 0
    for i in range(len(house)):
        min = -1
        for j in range(len(chicken)):
            hy, hx = house[i]
            cy, cx = chicken[j]
            dis = abs(cy-hy) + abs(cx-hx)

            if min == -1:
                min = dis
            elif dis < min:
                min = dis

        total_dis += min
    return total_dis

N, M = map(int, input().split(" "))
map = []
for i in range(N):
    map.append(input().split(" "))

house = []
chicken = []
choice = []
for i in range(N):
    for j in range(N):
        if map[i][j] == '1':
            house.append( (i+1, j+1) )
        elif map[i][j] == '2':
            chicken.append( (i+1, j+1) )

min = -1
dfs(house, chicken, M, choice)
print(min)