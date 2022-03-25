'''
### 소수 찾기 ###
[문제]
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

[입력]
- 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

[출력]
- 주어진 수들 중 소수의 개수를 출력한다.
'''

n = int(input())
nums = list(map(int, input().split()))

# 에라토스테네스의 체 알고리즘 활용
def prime_list(n):
    is_prime = [True] * (n+1)
    m = int(n ** 0.5)     # n의 약수는 sqrt(n)범위에 존재

    for i in range(2, m+1):  # 2부터 m+1개까지 확인
        if is_prime[i] == True:
            for j in range(i+i, n+1, i):  # i가 소수인 경우 i이상의 배수들을 False 판정
                is_prime[j] = False

    return [i for i in range(2, n+1) if is_prime[i] == True]

# nums 중 가장 큰 수까지 소수 리스트 찾기
primes = prime_list(1000)
print(len([num for num in nums if num in primes and num >= 2]))  # 2보다 크고, 소수인 수의 리스트 길이를 반환
