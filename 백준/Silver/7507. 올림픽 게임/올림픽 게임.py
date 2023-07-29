import heapq
import sys

T = int(sys.stdin.readline())

for iii in range(T):
    m = int(sys.stdin.readline())
    inform = []
    for i in range(m):
        d, s, e = sys.stdin.readline().split(" ")
        d = int(d)
        s = (int(s[:2]) * 60) + int(s[2:])
        e = (int(e[:2]) * 60) + int(e[2:])
        inform.append((e, s, d))

    day = 1
    sum = 0
    heap = []

    while inform:
        temp_list = []
        for i in range(len(inform)):
            if(inform[i][2] == day):
                heapq.heappush(heap, inform[i])
            else:
                temp_list.append(inform[i])

        if heap:
            min_e = heapq.heappop(heap)
            sum+=1

            while heap:
                temp = heapq.heappop(heap)
                if temp[1] >= min_e[0]:
                    sum+=1
                    min_e = temp[:]

        inform = temp_list.copy()
        day += 1

    print(f"Scenario #{iii+1}:")
    print(sum)
    print("")