"""
- 문제풀이
1. 테스트 케이스의 개수 t를 받아온다
2. for문을 range(t)만큼 실행한다
3. point변수를 0으로 선언한다 add_number의 변수를 1로 선언한다 그리고 last_char를 X로 선언한다
4. 입력되는 문자열을 받아 for문을 실행한다
5. last_char가 O이고 char값이 O라면 point += add_number해주고 add_number++를 진행한다
6. char값이 X라면 add_number을 1로 초기화 해준다
7. last_char에 char를 담아준다
8. 포인트를 출력한다
"""

t = int(input())

for _ in range(t):
    str = input()
    point = 0
    add_number = 1
    for char in str:
        if char == "O":
            point += add_number
            add_number += 1
        else:
            add_number = 1
    print(point)