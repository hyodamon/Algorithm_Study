import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    dp = [(1, 0), (0, 1)]
    zero = 0
    one = 0
    N = int(input())
    
    for i in range(2, N+1) :
        dp.append((dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1]))
    
    print(dp[N][0], dp[N][1])