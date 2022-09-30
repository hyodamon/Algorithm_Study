# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.
# 10 -> 2, 3 -> 0


import sys

N = int(sys.stdin.readline())

if N == 0 :
    print(0)
    exit()

def factorial(n) :
    if n > 2 :
        return n * factorial(n - 1)
    else :
        return n

F = factorial(N)

cnt = 0
for i in range(len(str(F)) - 1, -1, -1) :
    if str(F)[i] != '0' :
        break
    cnt += 1

print(cnt)