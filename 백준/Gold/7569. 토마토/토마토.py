import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())

box = []
tomatos = deque()
for i in range(H) :
    row = []
    for j in range(N) :
        row.append(list(map(int, input().split())))
        for k in range(M) :
            if row[j][k] == 1 :
                tomatos.append([i, j, k])
    box.append(row)

dr = [1, -1, 0, 0, 0, 0]
dc = [0, 0, 1, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

while tomatos :
    h, r, c = tomatos.popleft()
    for i in range(6) :
        nh, nr, nc = h + dh[i], r + dr[i], c + dc[i]
        if nh < 0 or nh >= H or nr < 0 or nr >= N or nc < 0 or nc >= M :
            continue

        if box[nh][nr][nc] == 0 :
            box[nh][nr][nc] = box[h][r][c] + 1
            tomatos.append([nh, nr, nc])
            
answer = 0
for h in range(H) :
    for r in range(N) :
        for c in range(M) :
            if box[h][r][c] == 0 :
                print(-1)
                exit()
            answer = max(answer, box[h][r][c])
print(answer - 1)