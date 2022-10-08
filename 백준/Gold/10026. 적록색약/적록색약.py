import sys
from collections import deque
sys.setrecursionlimit(6000)

input = sys.stdin.readline

N = int(input())
picture = []
weird_picture = []

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

visited1 = [[0 for _ in range(N)] for _ in range(N)]
visited2 = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(N) :
    tmp = []
    tmp2 = []
    for color in input().rstrip() :
        tmp.append(color)
        if color == 'G' :
            tmp2.append('R')
        else :
            tmp2.append(color)
    picture.append(tmp)
    weird_picture.append(tmp2)

def normal_dfs(r, c) :
    global flag
    for i in range(4) :
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < N and 0 <= nc < N :
            if visited1[nr][nc] == 0 and picture[r][c] == picture[nr][nc] :
                visited1[nr][nc] = flag
                normal_dfs(nr, nc)

def weird_dfs(r, c) :
    global flag
    for i in range(4) :
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < N and 0 <= nc < N :
            if visited2[nr][nc] == 0 and weird_picture[r][c] == weird_picture[nr][nc] :
                visited2[nr][nc] = flag
                weird_dfs(nr, nc)

flag = 1
for i in range(N) :
    for j in range(N) :
        if visited1[i][j] == 0 :
            normal_dfs(i, j)
            flag += 1
print(flag - 1, end=" ")

flag = 1
for i in range(N) :
    for j in range(N) :
        if visited2[i][j] == 0 :
            weird_dfs(i, j)
            flag += 1
print(flag - 1)