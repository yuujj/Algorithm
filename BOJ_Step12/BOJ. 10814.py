### 나이순 정렬 ###
n = int(input())
data = []

for i in range(n):
    a, b = map(str, input().split())
    data.append((i, int(a), b))

data = sorted(data, key=lambda x:(x[1], x[0]))

for d in data:
    print(d[1], d[2])