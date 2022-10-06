import sys
from collections import deque

N = int(sys.stdin.readline())

def D(n) :
    return n * 2 if n * 2 < 9999 else (n * 2) % 10000

def S(n) :
    return n - 1 if n > 0 else 9999

def L(n) :
    return (n % 1000) * 10 + (n // 1000)
    
def R(n) :
    return (n % 10) * 1000 + (n // 10)


def BFS(A, B) :
    queue = deque()
    queue.append((A, ''))
    visited = set()
    while queue :
        a, command = queue.popleft()
        Da, Sa, La, Ra = D(a), S(a), L(a), R(a)
        if a == B :
            print(command)
            return
        if Da not in visited :
            visited.add(Da)
            queue.append((Da, command + 'D'))
        if Sa not in visited :
            visited.add(Sa)
            queue.append((Sa, command + 'S'))
        if La not in visited :
            visited.add(La)
            queue.append((La, command + 'L'))
        if Ra not in visited :
            visited.add(Ra)
            queue.append((Ra, command + 'R'))
            
for _ in range(N) :
    A, B = map(int, sys.stdin.readline().split())
    BFS(A, B)