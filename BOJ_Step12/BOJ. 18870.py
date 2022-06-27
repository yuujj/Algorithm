### 정렬 - 좌표 압축 ###
n = int(input())
dots = list(map(int, input().split()))
dot_dict = {x:i for i, x in enumerate(sorted(list(set(dots))))}

for dot in dots:
    print(dot_dict[dot], end=' ')