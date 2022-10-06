import sys

N = int(sys.stdin.readline())

dp = [0 for _ in range(N)]

stairs = [0 for _ in range(N)]
for i in range(N) :
    stairs[i] = int(sys.stdin.readline())

for i in range(N) :
    if i == 0 :
        dp[i] = stairs[i]
    elif i == 1 :
        dp[i] = dp[i-1] + stairs[i]
    elif i == 2 :
        dp[i] = max(stairs[i-1] + stairs[i], stairs[i-2] + stairs[i])
    else :
        dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])
        
print(dp[N-1])