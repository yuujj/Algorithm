'''
### 골드바흐의 추측 ###
[문제]
1보다 큰 자연수 중에서  1과 자기 자신을 제외한 약수가 없는 자연수를 소수라고 한다.
예를 들어, 5는 1과 5를 제외한 약수가 없기 때문에 소수이다. 하지만, 6은 6 = 2 × 3 이기 때문에 소수가 아니다.
골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다.
이러한 수를 골드바흐 수라고 한다. 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다.
예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다.
10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.
2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오.
만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.

[입력]
- 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고 짝수 n이 주어진다.

[출력]
- 각 테스트 케이스에 대해서 주어진 n의 골드바흐 파티션을 출력한다. 출력하는 소수는 작은 것부터 먼저 출력하며, 공백으로 구분한다.
'''

import sys

# 에라토스테네스의 체 알고리즘 활용
def prime_list(n):
    is_prime = [True] * (n+1)
    m = int(n**0.5)

    for i in range(2, m+1):
        if is_prime[i] == True:
            for j in range(i+i, n+1, i):
                is_prime[j] = False

    return [i for i in range(2, n+1) if is_prime[i] == True]

primes = prime_list(10000)  # 소수 리스트 찾기

T = int(input())
for _ in range(T):
    n = int(sys.stdin.readline())

    if n // 2 in primes:   # 차이가 적은 것이 우선순위 -> 자기자신인 경우 출력
        print(n//2, n//2)
    else:
        primes_cand = [prime for prime in primes if prime <= n-2]

        # primes_cand 2개의 수를 더했을 때 n인 경우의 두 수와 두 수의 차이 -> list comprehension, 이를 두 수의 차이로 정렬하고 첫번째 값 가져오기
        answer = sorted([[i, j, abs(j-i)] for i in primes_cand for j in primes_cand if i!=j and i+j==n], key=lambda x:x[-1])[0]
        print(answer[0], answer[1])
