### 로또 ###
from itertools import combinations
while True:
    S = list(map(int, input().split()))
    if S == [0]:
        break

    k = S.pop(0)
    for comb in combinations(S, 6):
        print(' '.join(map(str, comb)))
    print()