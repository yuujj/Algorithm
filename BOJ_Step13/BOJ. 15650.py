### N과 M (2) ###
from itertools import combinations

n, m = map(int, input().split())
nums = list(range(1, n+1))

for comb in combinations(nums, m):
    print(' '.join(map(str, comb)))
