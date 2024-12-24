"""
- 문제풀이
1. 첫줄에 n을 변수에 담는다
2. 두번째 줄에 n개의 숫자를 리스트에 담는다
3. print할 정수의 갯수 answer을 0으로 선언
4. 리스트 for문
5. 나온 숫자 num를 2부터 num의 range로 for문 체크할 변수 하나를 true로 선언해준다
6. num%i가 0이 하나라도 존재하면 소수가 아니다
7. 두번째 for문이 끝났을 때 변수가 true면 소수 false면 소수가 아니기 때문에 true일 때만 
"""
import math

n = int(input())
numbers = list(map(int, input().split()))
answer = 0

for num in numbers:
    if num > 1:
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            answer += 1

print(answer)