'''
[분수 찾기]
분수의 순서에서 규칙을 찾는 문제

입력
첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.

출력
첫째 줄에 분수를 출력한다.
'''

x = int(input())

nums = 0
tmp = 0

while x > nums:
    tmp += 1
    nums += tmp

check = x - (nums - tmp)

# 짝수면 분자 증가, 분모 감소
if tmp % 2 == 0:
    i = check
    j = tmp - check + 1
# 홀수면 분자 감소, 분모 증가
else:
    j = check
    i = tmp - check + 1

print(str(i)+'/'+str(j))