# 분해합 
n = int(input())
def solution(n):
    d = [0] * (10000001)
    d[1], d[2] = 1, 1

    if n < 10 and n % 2 == 0:
        d[n] = n//2
        return d[n]
    else:
        N = n + sum(list(map(int, str(n))))

        maker = 10
        while maker <= N:
            nn = list(map(int, str(maker)))
            new_N = maker+sum(nn)
            if d[new_N] == 0:
                d[new_N] = maker
            maker += 1

        result = d[n]
        if result == n:
            return 0
        else:
            return result
print(solution(n))