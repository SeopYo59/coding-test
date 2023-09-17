N = int(input())
fac = 1
for i in range(1, N+1):
    fac = fac * i

temp = list(reversed(list(str(fac))))

cnt = 0
for i in range(N):
    if temp[i] == '0':
        cnt += 1

    else:
        break

print(cnt)