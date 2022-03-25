### N과 M (1) ###
from itertools import permutations

n, m = map(int, input().split())
nums = list(range(1, n+1))

for comb in permutations(nums, m):
    print(' '.join(map(str, comb)))
