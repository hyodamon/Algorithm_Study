import sys

N = int(sys.stdin.readline())
Ti = [0] * N
Pi = [0] * N

for i in range(N) :
    Ti[i], Pi[i] = list(map(int, sys.stdin.readline().split()))

dp = []

for i in range(0, N) :
    dp.append(Pi[i])
    if i + Ti[i] <= N : # (i + Ti[i])는 그 날로부터 상담을 완료하는 날
        for j in range(i) : 
            if j + Ti[j] <= i : 
                dp[i] = max(dp[i], dp[j] + Pi[i])
    else :
        dp[i] = 0
print(max(dp))