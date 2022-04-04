### 파도반 수열 ###
import sys
input = sys.stdin.readline
t = int(input())

n = [int(input()) for _ in range(t)]
nums = [1, 1, 1, 2, 2]

for i in range(5, max(n)):
    nums.append(nums[i-1]+nums[i-5])

for i in n:
    print(nums[i-1])