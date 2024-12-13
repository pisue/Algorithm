"""
1. 0보다 크거나 같은 정수 n이 주어진다
2. 이때, N!을 출력하는 프로그램을 작성하시오.
3. 0!=1 임을 생각할 것
"""
n = int(input())
result = 1
for i in range(1, n+1):
    result *= i
print(result)