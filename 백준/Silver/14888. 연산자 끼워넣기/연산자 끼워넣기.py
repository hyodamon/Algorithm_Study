import sys

N = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))
opers = list(map(int, sys.stdin.readline().split()))

minAnswer = 1e9
maxAnswer = -1e9

def DFS(idx, opers, result) :
    global minAnswer, maxAnswer
    if idx == N :
        minAnswer = min(minAnswer, result)
        maxAnswer = max(maxAnswer, result)
        return
    else :
        for i in range(4) :
            if opers[i] > 0 :
                opers[i] -= 1
                if i == 0 :
                    DFS(idx + 1, opers, result + nums[idx])
                elif i == 1 :
                    DFS(idx + 1, opers, result - nums[idx])
                elif i == 2 :
                    DFS(idx + 1, opers, result * nums[idx])
                elif i == 3 :
                    if result < 0 :
                        DFS(idx + 1, opers, -(-result // nums[idx]))
                    else :
                        DFS(idx + 1, opers, result // nums[idx])
                opers[i] += 1
        
        
        
DFS(1, opers, nums[0])
        
print(maxAnswer)
print(minAnswer)