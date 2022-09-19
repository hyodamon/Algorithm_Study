import sys

N = int(sys.stdin.readline())

juices = []

for _ in range(N) :
    juices.append(int(sys.stdin.readline()))
    
dp = [0] * N
dp[0] = juices[0]

for i in range(1, N) :
    if i == 1 :
        dp[i] = juices[i - 1] + juices[i]
    elif i == 2 :
        dp[i] = max(juices[i - 1] + juices[i], dp[i - 2] + juices[i], dp[i - 1])
    else :
        dp[i] = max(dp[i - 1], dp[i - 3] + juices[i - 1] + juices[i], dp[i - 2] + juices[i])
        
print(dp[N-1])