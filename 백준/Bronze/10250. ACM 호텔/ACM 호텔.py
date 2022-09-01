import sys

T = int(sys.stdin.readline())

for _ in range(T) : 
    H, W, N = map(int, sys.stdin.readline().split())

    n = 0
    for w in range(W) :
        for h in range(H) :
            n += 1
            if n == N :
                print("%d%s"%(h + 1, str(w + 1).zfill(2)))
                break
        else :
            continue
        break