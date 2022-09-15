import sys

input = sys.stdin.readline

N = int(input())
A = sorted(list(map(int, input().split())))

M = int(input())
B = list(map(int, input().split()))

dict = {}

for b in B :
    if b not in dict :
        cnt = 0
        start = 0
        last = N - 1
        while start <= last :
            mid = (start + last) // 2
            if b > A[mid] :
                start = mid + 1
            elif b < A[mid] :
                last = mid - 1
            else :
                cnt += 1
                # 왼쪽에 있는지 찾음
                prev = -1
                while mid + prev >= 0 and b == A[mid + prev] :
                    cnt += 1
                    prev -= 1
                    
                # 오른쪽에 있는지 찾음
                next = 1
                while mid + next < N and b == A[mid + next] :
                    cnt += 1
                    next += 1
                break
        dict[b] = cnt
    print(dict[b], end=" ")
        