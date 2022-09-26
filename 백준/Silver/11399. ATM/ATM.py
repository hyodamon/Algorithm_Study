import sys

N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))

P.sort()

answer = 0
sum = 0
for p in P :
    sum += p
    answer += sum
print(answer)