n = int(input())

for _ in range(n):
    arr = input().strip()  # 단일 문자열로 입력 받음
    count = 0
    is_valid = True
    for char in arr:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
        if count < 0:  # ')'가 '('보다 많은 경우
            is_valid = False
            break
    if is_valid and count == 0:  # 균형 잡힌 괄호 문자열인지 확인
        print("YES")
    else:
        print("NO")
