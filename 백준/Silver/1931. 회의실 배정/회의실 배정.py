import sys

N = int(sys.stdin.readline())
times = []

for _ in range(N) :
    start, end = map(int, sys.stdin.readline().split())
    times.append((end, start))
times.sort()

cnt = 1
prevEnd = times[0][0]

for i in range(1, N) :
    if times[i][1] >= prevEnd :
        cnt += 1
        prevEnd = times[i][0]

print(cnt)