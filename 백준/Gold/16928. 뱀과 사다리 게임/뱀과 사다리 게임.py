import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
MAP = [i for i in range(101)]

for _ in range(N) :
    x, y = map(int, input().split())
    MAP[x] = y

for _ in range(M) :
    u, v = map(int, input().split())
    MAP[u] = v

visited = [0 for i in range(101)]

queue = deque()
queue.append((1, 0))

while queue :
    pos, cnt = queue.popleft()
    for i in range(pos + 1, pos + 7) :
        nPos = MAP[i]
        if nPos >= 100 :
            print(cnt + 1)
            exit()
        if visited[i] == 0 :
            queue.append((nPos, cnt + 1))
            visited[i] = 1