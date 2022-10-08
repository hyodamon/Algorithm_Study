import sys
N = int(sys.stdin.readline())

video = []

for _ in range (N) :
    tmp = []
    for num in sys.stdin.readline().rstrip() :
        tmp.append(int(num))
    video.append(tmp)

answer = ""

def recursion(sr, sc, n) :
    global answer
    startNum = video[sr][sc]
    half = n // 2

    for r in range(sr, sr + n) :
        for c in range(sc, sc + n) :
            if startNum != video[r][c] :
                answer += "("
                recursion(sr, sc, half)
                recursion(sr, sc + half, half)
                recursion(sr + half, sc, half)
                recursion(sr + half, sc + half, half)
                answer += ")"
                return
    answer += str(startNum)
    
recursion(0, 0, N)
print(answer)