import sys
input = sys.stdin.readline
N, M = map(int, input().split())

paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cases = [[(0, 0), (0, 1), (1, 0), (1, 1)], 
         [(0, 0), (0, 1), (0, 2), (0, 3)], 
         [(0, 0), (1, 0), (2, 0), (3, 0)], 
         [(0, 0), (1, 0), (1, 1), (2, 1)],
         [(0, 1), (0, 2), (1, 0), (1, 1)],
         [(0, 1), (1, 0), (1, 1), (2, 0)],
         [(0, 0), (0, 1), (1, 1), (1, 2)],
         [(0, 0), (0, 1), (0, 2), (1, 1)],
         [(0, 1), (1, 0), (1, 1), (2, 1)],
         [(0, 1), (1, 0), (1, 1), (1, 2)],
         [(0, 0), (1, 0), (1, 1), (2, 0)],
         [(0, 0), (1, 0), (2, 0), (2, 1)],
         [(0, 0), (0, 1), (0, 2), (1, 0)],
         [(0, 0), (0, 1), (1, 1), (2, 1)],
         [(0, 2), (1, 0), (1, 1), (1, 2)],
         [(0, 1), (1, 1), (2, 0), (2, 1)],
         [(0, 0), (1, 0), (1, 1), (1, 2)],
         [(0, 0), (0, 1), (1, 0), (2, 0)],
         [(0, 0), (0, 1), (0, 2), (1, 2)]
        ]

answer = 0

for r in range(N) :
    for c in range(M) :
        for case in cases :
            value = 0 # 더한 값
            for pos in case :
                nr, nc = r + pos[0], c + pos[1]
                if 0 <= nr < N and 0 <= nc < M :
                    value += paper[nr][nc]
                else :
                    value = 0
                    break
            answer = max(answer, value)

print(answer)