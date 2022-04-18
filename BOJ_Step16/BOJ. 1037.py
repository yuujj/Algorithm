### 약수 - O ###
import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))

if n == 1:
    print(nums[0] * nums[0])
else:
    nums = sorted(nums)
    print(nums[0] * nums[-1])