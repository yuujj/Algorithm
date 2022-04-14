### ATM ###
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins = [coin for coin in coins if coin <= k]
cnt = 0
while coins:
    coin = coins.pop()
    mod, re = k // coin, k % coin
    cnt += mod
    k = re
print(cnt)