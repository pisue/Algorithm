"""
- 문제풀이
1. while True로 반복
2. 입력된 값을 받는다
3. 만약 입력받은 값이 0이면 break 
4. 입력받은 값과 문자열 역순이 같으면 yes 다르면 no를 리턴한다
"""
while True:
    n = input()  # 입력값을 받습니다
    if n == "0":  # 종료 조건 확인
        break
    # 문자열 역순 확인
    print("yes" if n == n[::-1] else "no")
        