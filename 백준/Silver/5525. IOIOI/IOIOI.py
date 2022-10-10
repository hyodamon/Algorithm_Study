import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

S = input().rstrip()

Pn = "IO" * N + "I"

cnt = 0
answer = 0
i = 0

while i < (M - 1) :
    if S[i : i+3] == 'IOI' :
        cnt += 1
        i += 2
        if cnt == N :
            cnt -= 1
            answer += 1
            
    else :
        i += 1
        cnt = 0
    
print(answer)