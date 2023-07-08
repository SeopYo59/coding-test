from collections import deque
import copy
def DFS(pointInform):
    stack = deque()
    stack.append(V)
    while stack:
        location = stack.pop()

        if pointInform[location][0] == 1:
            continue

        pointInform[location][0] = 1
        print(location, "", end='')

        pointInform[location][1].sort(reverse=True)
        for point in pointInform[location][1]:
            stack.append(point)

    print("")
def BFS(pointInform):
    queue = deque()
    queue.append(V)

    while queue:
        location = queue.popleft()

        if pointInform[location][0] == 1:
            continue

        pointInform[location][0] = 1
        print(location, "", end ='')

        pointInform[location][1].sort()
        for point in pointInform[location][1]:
            queue.append(point)

    print("")

# 1. 입력
N, M, V = map(int, input().split())

# 2. 점선과 간선 표현
pointInform = [None]

for i in range(N):
   pointInform.append([0, []])

for i in range(M):
   point1, point2 = map(int, input().split())
   pointInform[point1][1].append(point2)
   pointInform[point2][1].append(point1)
#print("정점과 간선 정보 확인", pointInform)

pointInform2 = copy.deepcopy(pointInform)

# 3. DFS, stack 사용
DFS(pointInform)

# 4. BFS, queue 사용
BFS(pointInform2)