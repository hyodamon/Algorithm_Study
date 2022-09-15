import sys
import heapq
input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    K = int(input())
    maxHeap, minHeap = [], []
    visited = [False] * K
    for key in range(K) :
        oper, num = input().split()
        num = int(num)
        if oper == 'I' :
            heapq.heappush(maxHeap, (-num, key))
            heapq.heappush(minHeap, (num, key))
            visited[key] = True
        elif oper == 'D' :
            if num == 1 :
                # maxHeap에 현재 값이 있고, 그 루트 값이 현재 False라면(이미 이전에 pop된)
                while maxHeap and visited[maxHeap[0][1]] == False :
                    heapq.heappop(maxHeap)
                # maxHeap 값의 루트 값을 없애준다. -> 최대값 제거
                if maxHeap :
                    visited[maxHeap[0][1]] = False # maxHeap에서 없애줬으니, 나중에 minHeap에서도 없애줘야 하므로 visited를 False로 바꿔준다.
                    heapq.heappop(maxHeap)

            elif num == -1 :
                while minHeap and visited[minHeap[0][1]] == False :
                    heapq.heappop(minHeap)
                if minHeap :
                    visited[minHeap[0][1]] = False
                    heapq.heappop(minHeap)
    while maxHeap and visited[maxHeap[0][1]] == False :
        heapq.heappop(maxHeap)
    while minHeap and visited[minHeap[0][1]] == False :
        heapq.heappop(minHeap)
                    
    print(f"{-maxHeap[0][0]} {minHeap[0][0]}" if maxHeap or minHeap else "EMPTY")