import sys

N = 1000 - int(sys.stdin.readline())

coins = [500, 100, 50, 10, 5, 1]
cnt = 0

for coin in coins :
    cnt += N // coin
    N %= coin
print(cnt)