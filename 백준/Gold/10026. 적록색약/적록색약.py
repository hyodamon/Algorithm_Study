import sys
from collections import deque
sys.setrecursionlimit(6000)

input = sys.stdin.readline

N = int(input())
normal_picture = []
weird_picture = []

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

for _ in range(N) :
    tmp = []
    tmp2 = []
    for color in input().rstrip() :
        tmp.append(color)
        if color == 'G' :
            tmp2.append('R')
        else :
            tmp2.append(color)
    normal_picture.append(tmp)
    weird_picture.append(tmp2)

def dfs(r, c, picture) :
    global flag
    for i in range(4) :
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < N and 0 <= nc < N :
            if visited[nr][nc] == 0 and picture[r][c] == picture[nr][nc] :
                visited[nr][nc] = flag
                dfs(nr, nc, picture)

flag = 1
visited = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N) :
    for j in range(N) :
        if visited[i][j] == 0 :
            dfs(i, j, normal_picture)
            flag += 1
print(flag - 1, end=" ")

flag = 1
visited = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N) :
    for j in range(N) :
        if visited[i][j] == 0 :
            dfs(i, j, weird_picture)
            flag += 1
print(flag - 1)