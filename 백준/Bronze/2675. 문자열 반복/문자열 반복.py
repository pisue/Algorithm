"""
- 문제풀이
1. 입력되는 값의 수 정수 n을 받는다
2. 반복문을 통해 입력되는 반복횟수 R와 문자열 S를 입력받는다
3. 출력할 변수를 선언한다
3. S의 len만큼 반복문을 통해 char에 r을 곱해 출력할 변수에 담는다
"""

n = int(input())

for _ in range(n):
    r, s = input().split()
    p = ""
    for char in s:
        p += char*int(r)
    print(p)
    