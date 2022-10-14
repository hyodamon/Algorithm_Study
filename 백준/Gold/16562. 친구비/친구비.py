import sys

N, M, k = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

friends = [x for x in range(N)]

def find(friend) :
    if friend != friends[friend] :
        friends[friend] = find(friends[friend])
    return friends[friend]

def union(friend1, friend2) :
    a = find(friend1)
    b = find(friend2)
    if a < b :
        friends[b] = a
    else :
        friends[a] = b
        
for _ in range(M) :
    v, w = map(int, sys.stdin.readline().split())
    union(v-1, w-1)

for i in range(N) :
    friends[i] = find(i)
cost = [0 for _ in range(N)]
n = 0

for i in friends :
    if cost[i] == 0 or cost[i] > A[n] :
        cost[i] = A[n]
    n += 1

totalCost = sum(cost)

if k < totalCost :
    print("Oh no")
else :
    print(totalCost)

