'''
### 소수 구하기 ###
[문제]
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

[입력]
- 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

[출력]
- 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
'''
m, n = map(int, input().split())

def prime_list(n):
    is_prime = [True] * (n+1)
    m = int(n ** 0.5)

    for i in range(2, m+1):
        if is_prime[i] == True:
            for j in range(i+i, n+1, i):
                is_prime[j] = False

    return [i for i in range(2, n+1) if is_prime[i] == True]

primes = prime_list(1000000)
target = [prime for prime in primes if m <= prime and prime <= n]  # m이상 n이하인 소수
for t in target:
    print(t)