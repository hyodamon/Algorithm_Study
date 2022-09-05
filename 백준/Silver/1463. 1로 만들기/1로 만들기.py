import sys
    
N = int(sys.stdin.readline())

dp = [0] * (N + 1)


for i in range(2,N+1):
    tmp = dp[i - 1]
    if i % 3 == 0:
        tmp = min(dp[i // 3], tmp)
    if i % 2 == 0:    
        tmp = min(dp[i // 2], tmp)
    dp[i] = tmp + 1

print(dp[N])