import sys
T = int(sys.stdin.readline())

for _ in range(T) :
    N = int(sys.stdin.readline())
    dp = [0] * 101
    
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2
    dp[6] = 3
    dp[7] = 4
    dp[8] = 5
    dp[9] = 7
    dp[10] = 9
    
    for i in range(10, N + 1) :
        dp[i] = dp[i-1] + dp[i-5]
    
    
    print(dp[N])