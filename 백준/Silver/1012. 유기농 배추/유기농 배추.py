import sys
from collections import deque
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

T = int(input())

def dfs(r, c) :
    visited[r][c] = 1
    for i in range(4) :
        nr, nc = r + dr[i], c + dc[i]
        if nr < 0 or nc < 0 or nr >= N or nc >= M :
            continue
        if visited[nr][nc] == 1 or farm[nr][nc] == 0 :
            continue
        visited[nr][nc] = 1
        dfs(nr, nc)

for _ in range(T) :
    M, N, K = map(int, input().split())
    answer = 0
    farm = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    
    for _ in range(K) :
        c, r = map(int, input().split())
        farm[r][c] = 1
    
    for r in range(N) :
        for c in range(M) :
            if farm[r][c] == 1 and visited[r][c] == 0 :
                answer += 1
                dfs(r, c)
    
    print(answer)