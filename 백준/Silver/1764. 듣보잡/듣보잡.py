import sys

N, M = map(int, sys.stdin.readline().split())

hash = dict()
doodbbo = []

for _ in range(N) :
    input = sys.stdin.readline()
    hash[input] = 1
    
for _ in range(M) :
    input = sys.stdin.readline()
    if hash.get(input) :
        hash[input] += 1

for name in hash.keys() :
    if hash[name] > 1 :
        doodbbo.append(name)

doodbbo.sort()

print(len(doodbbo))
for name in doodbbo :
    print(name, end="")