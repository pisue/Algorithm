"""
- 문제풀이
1. 시험 본 과목의 개수 N
2. 둘째 줄이 과목별 성적이 주어진다 리스트로 만든다
3. 리스트에서 최대값을 구한다
4. 각 리스트의 값을 최대값으로 나누고 100을 곱해준다
5. 리스트의 모든값을 더한 후 N으로 나눠 출력한다
"""

n = int(input())
numbers = list(map(int, input().split()))
max_num = max(numbers)

for i in range(n):
    numbers[i] = numbers[i]/max_num*100

print(sum(numbers)/n)
