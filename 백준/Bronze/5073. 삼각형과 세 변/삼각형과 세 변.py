while True:
    len = list(map(int, input().split(" ")))

    sum = 0
    for i in range(3):
        sum += len[i]
    if sum == 0:
        break

    sum = 0
    for i in range(3):
        if i != len.index(max(len)):
            sum += len[i]

    if sum <= max(len):
        print("Invalid")
        continue

    jud = 0
    for i in range(1, 3):
       if len[0] == len[i]:
           jud += 1

    if len[1] == len[2]:
        jud += 1

    if jud >= 2:
        print("Equilateral")
    elif jud == 1:
        print("Isosceles")
    elif jud == 0:
        print("Scalene")