### 좌표 정렬하기 2 ###
n = int(input())
dots = []
for _ in range(n):
    a, b = map(int, input().split())
    dots.append((a, b))
    
dots = sorted(dots, key=lambda x: (x[1], x[0]))

for dot in dots:
    print(dot[0], dot[1])