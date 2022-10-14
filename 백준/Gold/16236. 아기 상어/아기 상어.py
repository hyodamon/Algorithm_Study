import sys
from collections import deque
import heapq
sys.setrecursionlimit(1000000)

N = int(sys.stdin.readline())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

size = 2
cnt = 0

def DFS(st, sr, sc) :
    global size, cnt
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[sr][sc] = True
    queue = deque()
    queue.append((st, sr, sc))
    area = []
    minT = 1e9
    
    while queue :
        t, r, c = queue.popleft()
        for i in range(4) :
            nt, nr, nc = t + 1, r + dr[i], c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N or visited[nr][nc] :
                continue
            
            if size >= MAP[nr][nc] :
                if 0 < MAP[nr][nc] < size  :
                    if nt > minT :
                        break
                    else :
                        minT = nt
                    heapq.heappush(area, (nt, nr, nc))
                else :
                    queue.append((nt, nr, nc))
                    visited[nr][nc] = True

    if area :
        newT, newR, newC = heapq.heappop(area)
        MAP[sr][sc] = 0
        MAP[newR][newC] = 9
        
        cnt += 1
        if size == cnt :
            size += 1
            cnt = 0
        DFS(newT, newR, newC)
    else :
        print(st)
    
for i in range(N) :
    for j in range(N) :
        if MAP[i][j] == 9 :
            DFS(0, i, j)
            break
    else: 
        continue
    break