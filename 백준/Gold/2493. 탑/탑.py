N = int(input())
tops = list(map(int, input().split(" ")))

stack = []
answer = ['?'] * N

for i in range(N):
    if not stack:
        stack.append(i)

    else:
        if tops[i] >= tops[stack[len(stack)-1]]:
            while stack and tops[i] >= tops[stack[len(stack)-1]]:
                index = stack.pop()

                if stack:
                    answer[index] = stack[len(stack)-1] + 1
                else:
                    answer[index] = 0

            stack.append(i)

        else:
            stack.append(i)

while stack:
    index = stack.pop()

    if stack:
        answer[index] = stack[len(stack) - 1] + 1
    else:
        answer[index] = 0

for i in range(N):
    print(answer[i], end = " ")