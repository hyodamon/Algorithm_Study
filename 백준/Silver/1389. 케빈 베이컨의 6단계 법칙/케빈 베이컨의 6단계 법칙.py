from re import L
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[1e9 for _ in range(N)] for _ in range(N)]

for _ in range(M) :
    A, B = map(int, input().split())
    graph[A-1][B-1] = 1
    graph[B-1][A-1] = 1

for k in range(N) :
    for i in range(N) :
        for j in range(N) :
            if graph[i][k] + graph[k][j] < graph[i][j] :
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(N) :
    graph[i][i] = 0


minKevinBaker = 1e9
answer = 0

for i in range(N) :
    tmp = sum(graph[i])
    if minKevinBaker > tmp :
        minKevinBaker = tmp
        answer = i + 1
        
print(answer)