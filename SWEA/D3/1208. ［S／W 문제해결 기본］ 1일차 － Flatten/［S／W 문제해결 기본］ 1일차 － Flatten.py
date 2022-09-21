T = 10

for test_case in range(1, T + 1):
    N = int(input())
    boxs = list(map(int, input().split()))
    
    boxs.sort()
    for _ in range(N) :
        boxs[0] += 1
        boxs[-1] -= 1
        boxs.sort()
    
    result = boxs[-1] - boxs[0]
    print(f'#{test_case} {result}')
