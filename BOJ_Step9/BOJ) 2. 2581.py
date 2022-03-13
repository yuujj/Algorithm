'''
### 소수 ###
[문제]
자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.
예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.

[입력]
- 입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.
- M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.

[출력]
- M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다.
- 단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.
'''
m = int(input())
n = int(input())

# 에라스테네스의 체 알고리즘 활용
def prime_list(n):
    is_prime = [True] * (n+1)
    m = int(n**0.5)

    for i in range(2, m+1):
        if is_prime[i] == True:
            for j in range(i+i, n+1, i):
                is_prime[j] = False

    return [i for i in range(2, n+1) if is_prime[i] == True]

primes = prime_list(10001)  # 10001까지의 소수 리스트 추출 (n 넣어도 됨)
target = [prime for prime in primes if m <= prime and n >= prime]  # m이상 n이하인 소수 리스트값 추출
if target == []:
    print(-1)
else:
    print(sum(target)) # 타겟의 합
    print(min(target)) # 타겟의 최솟값
