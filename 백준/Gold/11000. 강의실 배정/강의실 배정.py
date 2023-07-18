import heapq
def add_class(nextclass, classroom):
         if classroom and nextclass[0] >= classroom[0]:
             heapq.heappop(classroom)
             heapq.heappush(classroom, nextclass[1])
             return

         heapq.heappush(classroom, nextclass[1])
         return

N = int(input())

class_inform = []
for i in range(N):
    s, t = map(int, input().split())
    heapq.heappush(class_inform, (s, t))

classroom = []
for i in range(N):
    nextclass = heapq.heappop(class_inform)
    add_class(nextclass, classroom)

print(len(classroom))