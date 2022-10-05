import sys
input = sys.stdin.readline

N = int(input())

# 어차피 100에서 시작이므로
if N == "100" :
    print(0)
    exit()

M = int(input())

# 고장난 버튼을 빼기 위해 set과 차집합 이용
nums = {str(i) for i in range(10)}
breaks = set(input().split())
nums -= breaks

answer = abs(N - 100)

for num in range(1000000):
    num = str(num)
    
    flag = True
    for n in num:
        if n not in nums:
            flag = False
            break

    if flag : 
        answer = min(answer, abs(int(num) - N) + len(num))
            

print(answer)