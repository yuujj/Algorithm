### 좌표 정렬하기 ###
n = int(input())
dots = []
for _ in range(n):
    a, b = map(int, input().split())
    dots.append((a, b))

dots = sorted(dots, key=lambda x: (x[0],x[1]))
for dot in dots:
    print(dot[0], dot[1])