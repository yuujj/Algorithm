'''
### 베르트랑 공준 ###

[문제]
베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.
이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.
예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)
자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오.

[입력]
- 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 케이스는 n을 포함하는 한 줄로 이루어져 있다.
- 입력의 마지막에는 0이 주어진다.

[출력]
- 각 테스트 케이스에 대해서, n보다 크고, 2n보다 작거나 같은 소수의 개수를 출력한다.
'''

import sys
n = -1

def prime_list(n):
    is_prime = [True] * (n + 1)
    m = int(n ** 0.5)

    for i in range(2, m + 1):
        if is_prime[i] == True:
            for j in range(i + i, n + 1, i):
                is_prime[j] = False

    return [i for i in range(2, n + 1) if is_prime[i] == True]


while True:   # 0이 입력으로 들어올때까지 반복
    n = int(input())
    if n == 0:         # 0이 들어오면 멈춤
        break

    primes = prime_list(2*n)  # 2n개 까지의 소수 리스트
    print(len([prime for prime in primes if n < prime]))  # n 초과인 경우만 추출, 길이 반환