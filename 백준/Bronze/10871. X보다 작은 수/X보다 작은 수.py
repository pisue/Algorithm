"""
- 문제풀이
1. 첫째줄에 n과 x가 주어진다 두째줄에 수열 a를 이루는 정수는 n개가 주어진다
2. x보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다
"""

n, x = map(int, input().split())
numbers = list(map(int, input().split()))
filtered_numbers = []
for num in numbers:
    if num < x:
        filtered_numbers.append(num)
print(" ".join(map(str, filtered_numbers)))
