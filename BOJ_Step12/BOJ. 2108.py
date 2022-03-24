### 통계학 ###
import sys
from collections import Counter
n = int(input())
nums = [int(sys.stdin.readline().strip()) for _ in range(n)]

sum_num = sum(nums)
len_num = len(nums)

# 산술평균
print(round(sum_num/len_num))

# 중앙값
print(sorted(nums)[len_num//2])

# 최빈값 - 카운트 리스트 만들어서 2개 이상인 경우 2번째
def modes(numbers):
    cnt = Counter(nums)
    order = cnt.most_common()
    maximum = order[0][1]

    modes = []
    for num in order:
        if num[1] == maximum:
            modes.append(num[0])
    return sorted(modes)
mode = modes(nums)

if len(mode) > 1:
    print(mode[1])
else:
    print(mode[0])

# 범위
print(max(nums)-min(nums))