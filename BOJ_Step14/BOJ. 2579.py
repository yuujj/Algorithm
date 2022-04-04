### 계단 오르기 ###
import sys
input = sys.stdin.readline

t = int(input())
stairs = [int(input()) for _ in range(t)]
steps = []

if t < 3:
    print(sum(stairs))

else:
    steps.append(stairs[0])
    steps.append(max(stairs[0]+stairs[1],stairs[1]))
    steps.append(max(stairs[0]+stairs[2],stairs[1]+stairs[2]))

    for i in range(3, t):
        steps.append(max(steps[i-2]+stairs[i], steps[i-3]+stairs[i]+stairs[i-1]))

    print(steps[-1])