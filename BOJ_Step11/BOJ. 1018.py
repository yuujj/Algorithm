### 체스판 다시 칠하기 ###
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [input() for _ in range(n)]

# 'W'로 시작
def check_line(line, start):
    cnt = 0
    for idx, v in enumerate(line):
        # 인덱스가 짝수인 경우 : start와 같아야함
        if idx % 2 == 0:
            if v != start:
                cnt += 1
        # 인덱스가 홀수인 경우 : start와 달라야함
        else:
            if v == start:
                cnt += 1
    return cnt

total = 9999

for n_end in range(8, n+1):
    n_start = n_end-8

    for m_end in range(8, m+1):
        m_start = m_end-8

        temp_board = board[n_start:n_end]
        start_w, start_b = 0, 0
        w_cnt, b_cnt = 0, 0

        for idx, lines in enumerate(temp_board):
            line = lines[m_start:m_end]
            if idx % 2 == 0:
                case1, case2 = 'W', 'B'
            else: 
                case1, case2 = 'B', 'W'

            # w로 시작하는 경우
            w_cnt = check_line(line, case1)
            start_w += w_cnt

            # b로 시작하는 경우
            b_cnt = check_line(line, case2)
            start_b += b_cnt

        # 가장 적게 변해도 되는 경우 저장
        temp_total = min(start_w, start_b)
        if temp_total < total:
            total = temp_total

print(total)