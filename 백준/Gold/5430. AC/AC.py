import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

def R(arr) :
    result = deque()
    for i in range(len(arr) - 1, -1, -1) :
        result.append(arr[i])
    return result

for _ in range(T) :
    P = input().rstrip()
    N = int(input())
    inputX = input().rstrip()
    
    X = deque(inputX[1:-1].split(','))
    if inputX == "[]" :
        X = deque()
    
    cntD = 0
    cntR = 0
    for p in P :
        if p == 'D' :
            cntD += 1
        elif p == 'R' :
            cntR += 1
             
    if cntD > len(X) :
        print("error")
        continue
    
    isReverse = False
    for p in P :
        if p == 'R' :
            if isReverse :
                isReverse = False
            else :
                isReverse = True
        elif p == 'D' :
            if isReverse : 
                X.pop()
            else :         
                X.popleft()

    if isReverse :
        X = R(X)

    print(f'[{",".join(X)}]')