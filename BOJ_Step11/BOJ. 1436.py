n = int(input())

movie = 666
cnt = 0
while 1:
    # 666이 있다면 cnt+1
    if '666' in str(movie):
        cnt += 1
    # cnt가 n과 같으면 출력
    if cnt == n:
        print(movie)
        break
    movie += 1