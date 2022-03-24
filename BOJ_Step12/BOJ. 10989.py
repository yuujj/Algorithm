### 수 정렬하기 3 ###
import sys
from collections import defaultdict

n = int(input())
d = defaultdict(int)

for i in range(n):
    num = int(sys.stdin.readline().strip())
    d[num] += 1

keys = sorted(d.keys())

for key in keys:
    for i in range(d[key]):
        print(key)
