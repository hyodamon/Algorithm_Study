import sys

N, M = map(int, sys.stdin.readline().split())

def DFS(n) :
    if n == M :
        for r in result :
            print(r, end=' ')
        print()
    else :
        for i in range(N) :
            if checklist[i] == False :
                result[n] = nums[i]
                checklist[i] = True
                DFS(n + 1)
                checklist[i] = False


nums = [i + 1 for i in range(N)]
result = [0] * M
checklist = [False] * (N + 1)

DFS(0)
