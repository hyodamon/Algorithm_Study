import sys
from collections import deque

N = int(sys.stdin.readline())

Map = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def BFS(sr, sc) :
    queue = deque()    
    queue.append((sr, sc))
    houseCnt = 1
    while queue :
        r, c = queue.popleft()
        for i in range(4) :
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N :
                if Map[nr][nc] == 1 and visited[nr][nc] == 0 :
                    queue.append((nr, nc))
                    visited[nr][nc] = 1
                    houseCnt += 1
    return houseCnt

visited = [[0 for _ in range(N)] for _ in range(N)]

danjiCnt = 0
houseCnt = []
for i in range(N) :
    for j in range(N) :
        if Map[i][j] == 1 and visited[i][j] == 0 :
            visited[i][j] = 1
            danjiCnt += 1
            houseCnt.append(BFS(i, j))

print(danjiCnt)
houseCnt.sort()
for cnt in houseCnt :
    print(cnt)