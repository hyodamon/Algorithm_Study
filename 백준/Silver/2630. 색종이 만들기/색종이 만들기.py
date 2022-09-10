import sys

N = int(sys.stdin.readline())

paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

blue = 0
white = 0

def recursion(n, r, c) :
    global blue, white
    sum = 0
    
    tmp = paper[r][c]
    for i in range(r, r + n) :
        for j in range(c, c + n) :
            if paper[i][j] != tmp :
                half = n // 2
                recursion(half, r, c)
                recursion(half, r + half, c)
                recursion(half, r, c + half)
                recursion(half, r + half, c + half)
                return
            
    if tmp == 1 :
        blue += 1
    else :
        white += 1
    

recursion(N, 0, 0)

print(white)
print(blue)