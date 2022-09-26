import sys

T = int(sys.stdin.readline())

for _ in range(T) :
    
    N = int(sys.stdin.readline())
    dp = [1] * 12
    dp[2] = 2
    dp[3] = 4
    
    if N > 3 :
        for i in range(3, N + 1) :
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
            
    print(dp[N])