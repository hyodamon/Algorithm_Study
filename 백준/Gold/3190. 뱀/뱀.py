import sys
from collections import deque

input = sys.stdin.readline

dir = [(0, 1), (-1, 0), (0, -1), (1, 0)]

N = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]
snake = deque()
    
K = int(input())
for _ in range(K) :
    tmp = list(map(int, input().split()))
    r, c = tmp[0] - 1, tmp[1] - 1
    board[r][c] = 2

L = int(input())
X = []
C = []

for _ in range(L) :
    tmp = list(map(str, input().split()))
    X.append(int(tmp[0]))
    C.append(tmp[1])
    
idx = 0
cnt = 0
hr, hc = 0, 0
dirIdx = 0

while True :
    board[hr][hc] = 1
    snake.append((hr, hc))
    
    if idx < L and cnt == X[idx] : # 방향 바꿈
        if C[idx] == 'L' :
            dirIdx = (dirIdx + 1) % 4
        elif C[idx] == 'D' :
            dirIdx = (dirIdx - 1) % 4
        idx += 1
        
    hr, hc = hr + dir[dirIdx][0], hc + dir[dirIdx][1]
    if (hr < 0 or hc < 0 or hr >= N or hc >= N) or board[hr][hc] == 1 :
        break

    if board[hr][hc] == 2 :
        board[hr][hc] = 1
        cnt += 1
        continue
    
    tr, tc = snake.popleft()
    board[tr][tc] = 0
    cnt += 1
print(cnt + 1)