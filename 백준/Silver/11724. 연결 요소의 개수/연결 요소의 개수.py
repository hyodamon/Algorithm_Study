import sys
from collections import deque
sys.setrecursionlimit(5000)

N, M = map(int, sys.stdin.readline().split())

graph = {}
visited = [False] * (N + 1)

for _ in range(M) :
    u, v = map(int, sys.stdin.readline().split())
    if u in graph :
        graph[u].append(v)
    else :   
        graph[u] = [v]
    if v in graph :
        graph[v].append(u)
    else :
        graph[v] = [u]

def DFS(node) :
    visited[node] = True
    if node in graph :
        for nextNode in graph[node] :
            if visited[nextNode] == False :
                DFS(nextNode)
    return 1

cnt = 0
for node in range(1, N + 1) :
    if visited[node] == False :
        cnt += DFS(node)
        
print(cnt)