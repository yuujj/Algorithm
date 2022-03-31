### 피보나치 함수 ###
import sys

T = int(input())
# data = sys.stdin.readline().rstrip()
data = []
for t in range(T):
    data.append(int(input()))


fib_0 = [0] * 41
fib_1 = [0] * 41

def fibonacci(n):
    if n == 0:
        fib_0[n] = 1
        fib_1[n] = 0
        return fib_0[n], fib_1[n]
    elif n == 1:
        fib_0[n] = 0
        fib_1[n] = 1
        return fib_0[n], fib_1[n]

    if fib_0[n] != 0 and fib_1[n] != 0:
        return fib_0[n], fib_1[n]
    else:
        fib_0_tmp1, fib_1_tmp1 = fibonacci(n-1)
        fib_0_tmp2, fib_1_tmp2 = fibonacci(n-2)
        fib_0[n], fib_1[n] = fib_0_tmp1+fib_0_tmp2, fib_1_tmp1+fib_1_tmp2
        return fib_0[n], fib_1[n]

for i in data:
    fib0, fib1 = fibonacci(i)
    print(fib0, fib1)
