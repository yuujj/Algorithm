### 최소공배수 - O ###
import sys, math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(math.lcm(a, b))