"""
- 문제풀이
1. n, k의 값을 받는다
2. 이항계수를 계산한다
"""
n, k = map(int, input().split())

# 이항 계수 계산
result = 1
for i in range(k):
    result *= (n - i)
    result //= (i + 1)

print(result)
