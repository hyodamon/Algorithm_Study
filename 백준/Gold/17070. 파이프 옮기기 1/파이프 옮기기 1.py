import sys

input = sys.stdin.readline

N = int(input())

house = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
def DFS(hr, hc, tr, tc, state) :
    global cnt
    if hr == (N - 1) and hc == (N - 1) :
        cnt += 1       
    else :
        if state == 0 : # 가로
            if hc + 1 < N and house[hr][hc + 1] == 0  :
                DFS(hr, hc + 1, hr, hc, 0)
            if hr + 1 < N and hc + 1 < N and house[hr + 1][hc + 1] == 0 and house[hr][hc + 1] == 0 and house[hr + 1][hc] == 0 :
                DFS(hr + 1, hc + 1, hr, hc, 2)
        elif state == 1 : # 세로
            if hr + 1 < N and house[hr + 1][hc] == 0 :
                DFS(hr + 1, hc, hr, hc, 1)
            if hr + 1 < N and hc + 1 < N and house[hr + 1][hc + 1] == 0 and house[hr][hc + 1] == 0 and house[hr + 1][hc] == 0 :
                DFS(hr + 1, hc + 1, hr, hc, 2)
        elif state == 2 : # 대각선 
            if hc + 1 < N and house[hr][hc + 1] == 0 :
                DFS(hr, hc + 1, hr, hc, 0)
            if hr + 1 < N and house[hr + 1][hc] == 0 :
                DFS(hr + 1, hc, hr, hc, 1)
            if hr + 1 < N and hc + 1 < N and house[hr + 1][hc + 1] == 0 and house[hr][hc + 1] == 0 and house[hr + 1][hc] == 0 :
                DFS(hr + 1, hc + 1, hr, hc, 2)
    
DFS(0, 1, 0, 0, 0)

print(cnt)
