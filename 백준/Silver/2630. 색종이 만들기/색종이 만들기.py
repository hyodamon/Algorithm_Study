import sys

N = int(sys.stdin.readline())

paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

blue = 0
white = 0

def recursion(n, r, c) :
    global blue, white
    sum = 0
    
    for i in range(r, r + n) :
        for j in range(c, c + n) :
            sum += paper[i][j]
    if sum == n ** 2 :
        blue += 1
    elif sum == 0 :
        white += 1
    else :
        half = n // 2
        recursion(half, r, c)
        recursion(half, r + half, c)
        recursion(half, r, c + half)
        recursion(half, r + half, c + half)
    

recursion(N, 0, 0)

print(white)
print(blue)