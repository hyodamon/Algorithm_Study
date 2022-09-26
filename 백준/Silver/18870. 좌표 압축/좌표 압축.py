import sys

N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))

d = dict()

_X = [0] * N
for i in range(N) :
    _X[i] = X[i]
    
X = set(X)
X = list(X)
X.sort(reverse = True)

n = len(X) - 1
for x in X :
    d[x] = n
    n -= 1
    
for x in _X :
    print(d[x], end=" ")