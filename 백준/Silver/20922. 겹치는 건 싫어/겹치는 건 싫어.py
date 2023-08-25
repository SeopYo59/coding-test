N, K = map(int, input().split(" "))

seq = list(map(int, input().split(" ")))
count = [0 for i in range(100001)]

startp = 0
endp = 0
len = 0
max = 0

while endp != N:
    count[seq[endp]] += 1
    len += 1

    if count[seq[endp]] > K:
        if max < len:
            max = len - 1

        while seq[startp] != seq[endp]:
            count[seq[startp]] -= 1
            len -= 1
            startp += 1
        count[seq[startp]] -= 1
        len -= 1
        startp += 1

    endp += 1

if max < len:
    max = len

print(max)