import sys

N = int(sys.stdin.readline())

answers = {-1: 0, 0: 0, 1:0}
papers = []

for _ in range(N) :
    tmp = list(map(int, sys.stdin.readline().split()))
    papers.append(tmp)

def recursion(sr, sc, n) :
    if n < 1 :
        return
    
    startNum = papers[sr][sc]
    cutNum = n // 3
    
    for r in range(sr, sr + n) :
        for c in range(sc, sc + n) :
            if papers[r][c] != startNum :
                recursion(sr, sc, cutNum)
                recursion(sr + cutNum, sc, cutNum)
                recursion(sr + cutNum * 2, sc, cutNum)
                
                recursion(sr, sc + cutNum, cutNum)
                recursion(sr + cutNum, sc + cutNum, cutNum)
                recursion(sr + cutNum * 2, sc + cutNum, cutNum)
                
                recursion(sr, sc + cutNum * 2, cutNum)
                recursion(sr + cutNum, sc + cutNum * 2, cutNum)
                recursion(sr + cutNum * 2, sc + cutNum * 2, cutNum)
                return
    answers[startNum] += 1
                
    
recursion(0, 0, N)

for answer in answers.values() :
    print(answer)
    