import sys
from tabnanny import check

N, M = map(int, sys.stdin.readline().split())

def DFS(n, start) :
    if n == M :
        print(' '.join(map(str, result)))
    else :
        for i in range(start, N) :
            result[n] = nums[i]
            DFS(n + 1, i)
    
    
nums = [i + 1 for i in range(N)]
result = [0] * M
checklist = [0] * (N + 1)

DFS(0, 0)