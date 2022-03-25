### N과 M (4) ###
from itertools import combinations_with_replacement
n, m = map(int, input().split())
nums = list(range(1, n+1))

for comb in combinations_with_replacement(nums, m):
    print(' '.join(map(str, comb)))