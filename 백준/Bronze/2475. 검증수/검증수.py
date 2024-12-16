"""
- 문제풀이
1. 공백을두고 주어진 5개의 숫자를 리스트에 담는다
2. for문으로 해당 값을 제곱해 특정변수에 더해준다
3. for문이 끝나면 10으로 나눈 나머지 값을 출력한다
"""

numbers = list(map(int, input().split()))
answer = 0
for n in numbers:
    answer += n*n

print(answer%10)