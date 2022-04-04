### RGB거리 ###
n = int(input())
houses = []

for _ in range(n):
    houses.append(list(map(int, input().split())))

for i in range(1, n):
    houses[i][0]= min(houses[i-1][1], houses[i-1][2]) + houses[i][0]  # 빨간집
    houses[i][1]= min(houses[i-1][0], houses[i-1][2]) + houses[i][1]  # 초록집
    houses[i][2]= min(houses[i-1][0], houses[i-1][1]) + houses[i][2]  # 파란집
print(min(houses[n-1]))
