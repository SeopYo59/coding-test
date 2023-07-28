import sys

T = int(sys.stdin.readline())

def cal_dp(coin, M):
    dp = [0] * (M + 1)
    dp[0] = 1

    for i in range(len(coin)):
        for j in range(coin[i], M+1):
            dp[j] += dp[j - coin[i]]
    return dp[M]

for i in range(T):
    N = int(sys.stdin.readline())
    coin = list(map(int, input().split(" ")))
    M = int(sys.stdin.readline())

    print(cal_dp(coin, M))