import heapq
import sys

input = sys.stdin.readline

N = int(input())

heap = []

for _ in range(N) :
    tmp = int(input())
    num = (abs(tmp), tmp)
    
    if tmp == 0 : 
        if heap :
            print(heapq.heappop(heap)[1])
        else : 
            print(0)
    else :
        heapq.heappush(heap, num)