### 수 정렬하기 2 ###
import sys
N = int(input())
num = []
for _ in range(N):
    num.append(int(sys.stdin.readline()))

num.sort()
for i in num:
    print(i)