### N과 M (3) ###
from itertools import product

n, m = map(int, input().split())
nums = list(range(1, n+1))

for comb in product(nums, repeat=m):
    print(' '.join(map(str, comb)))