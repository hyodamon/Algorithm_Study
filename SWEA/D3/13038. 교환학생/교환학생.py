T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    
    
    
    firstDayList = []
    
    for i in range(len(A)) :
        if A[i] == 1 :
            firstDayList.append(i)
            
    answer = 1e9
    
    for day in firstDayList :
        dayCnt = 0
        classCnt = 0
        while classCnt < N :
            if A[day] == 1 :
                classCnt += 1
            dayCnt += 1
            if day > 5 :
                day = 0
            else :
                day += 1
        answer = min(answer, dayCnt)
        
    print(f'#{test_case} {answer}')