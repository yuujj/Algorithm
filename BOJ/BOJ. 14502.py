### 연구소 ###
n, m = map(int, input().split())
maps = []
safe_zone, virus_zone = [], []
safety = 0

for _n in range(n):
    line = list(map(int, input().split()))
    maps.append(line)

    # 0인 곳 정보 저장
    for idx, l in enumerate(line):
        if l == 0:
            safe_zone.append((_n, idx))
        elif l == 2:
            virus_zone.append((_n, idx))


# safe zone 중에서 3군데에 벽을 설치한다
# 바이러스를 퍼뜨린다. -> dfs
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx and nx < n and 0 <= ny and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

# 안전지대의 개수를 센다
def count_safe_zone(arr):
    cnt = sum([arr[i].count(0) for i in range(len(arr))])
    return cnt


# 키 3개의 조합
for a in range(len(safe_zone)):
    for b in range(len(safe_zone)):
        for c in range(len(safe_zone)):
            if a != b and a != c and b != c:
                temp = [[j for j in maps[i]] for i in range(len(maps))]
                x1, y1 = safe_zone[a]
                x2, y2 = safe_zone[b]
                x3, y3 = safe_zone[c]

                temp[x1][y1] = 1
                temp[x2][y2] = 1
                temp[x3][y3] = 1

                # 바이러스 퍼뜨리기
                for v in virus_zone:
                    x, y = v
                    virus(x, y)

                safety = max(safety, count_safe_zone(temp))

print(safety)
