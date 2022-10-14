import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    M, N, x, y = map(int, input().split())
    
    cnt = -1
    while x <= M * N :
        if x % N == y % N :
            cnt = x
            break
        x += M
    print(cnt)
