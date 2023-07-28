import sys

def cal(inform):
    if len(inform) == 1:
        print("YES")
        return

    s1 = inform[0: int(len(inform) / 2)]
    s2 = inform[int(len(inform) / 2) + 1:]
    s2 = list(s2)
    s2.reverse()
    s2 = "".join(s2)

    for i in range(len(s1)):
        if s1[i] == s2[i]:
            print("NO")
            return
    cal(s1)

T = int(sys.stdin.readline())

for i in range(T):
    inform = sys.stdin.readline().strip()
    cal(inform)