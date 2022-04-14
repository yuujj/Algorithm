### 주유소 ###
import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

total_cost = 0

min_cost = cost[0]
total_cost = min_cost * dist[0]

for i in range(1, len(dist)):
    if cost[i] < min_cost:
        min_cost = cost[i]

    total_cost += min_cost * dist[i]
print(total_cost)