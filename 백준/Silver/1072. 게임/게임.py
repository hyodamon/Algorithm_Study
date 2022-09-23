import sys
X, Y = map(int, sys.stdin.readline().split())

Z = (100 * Y) // X
if Z == 100 or Z == 99 :
    print(-1)
    exit()
    
cnt = 0
left = 1
right = X

while left <= right :
    mid = (left + right) // 2
    if ((Y + mid) * 100) // (X + mid) <= Z :
        left = mid + 1
    else :
        cnt = mid
        right = mid -1
    
print(cnt)