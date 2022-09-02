import sys

N = int(sys.stdin.readline())

dp = [0] * (N + 1)
dp[0] = 0 
dp[1] = 1

for i in range(2, N + 1) :
    minNum = 50001
    
    for j in range(1, int(i ** 0.5) + 1) :
        minNum = min(minNum, dp[i - j ** 2])
        
    dp[i] = minNum + 1
    

print(dp[-1])