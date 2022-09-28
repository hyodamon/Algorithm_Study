import sys
import heapq

N = int(sys.stdin.readline())
maxheap = []
for _ in range(N) :
    x = int(sys.stdin.readline())
    if x == 0 :
        if len(maxheap) == 0 :
            print(0)
        else :
            print(heapq.heappop(maxheap))  
    else :
        heapq.heappush(maxheap, x)