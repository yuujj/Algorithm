### 링 - O ###
import sys, math
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

a = nums[0]
for i in range(1, len(nums)):
    gcd = math.gcd(a, nums[i])
    print('{}/{}'.format(a//gcd, nums[i]//gcd))

