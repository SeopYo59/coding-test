N, K = map(int, input().split())
seq = list(input().split(" "))
seq.append('none')

startp = 0
endp = 0
cnt = 0
len = 1
min = 10000000

while True:
    if cnt == K:

        while True:
            if len - 1 < min:
                min = len - 1

            if seq[startp] != '1':
                startp += 1
                len -= 1

            elif seq[startp] == '1':
                if endp == N:
                    if min == 10000000: print("-1")
                    else: print(min)
                    exit(0)

                startp += 1
                len -= 1
                cnt -= 1
                break

    if len - 1 == N:
        print("-1")
        exit(0)

    if endp == N and cnt < K:
        if endp == N:
            if min == 10000000:
                print("-1")
            else:
                print(min)
            exit(0)

    if seq[endp] == '1':
        cnt += 1

    endp += 1
    len += 1