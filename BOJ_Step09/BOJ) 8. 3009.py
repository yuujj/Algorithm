'''
### 네 번째 점 ###
[문제]
세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

[입력]
- 세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

[출력]
- 직사각형의 네 번째 점의 좌표를 출력한다.
'''

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

if x1 == x2:
    ans_x = x3
elif x2 == x3:
    ans_x = x1
else:
    ans_x = x2

if y1 == y2:
    ans_y = y3
elif y2 == y3:
    ans_y = y1
else:
    ans_y = y2

print(ans_x, ans_y)