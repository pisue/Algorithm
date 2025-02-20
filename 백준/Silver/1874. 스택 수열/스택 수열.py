n = int(input())
stack = []
cmd = []

next_num = 1 # 1부터 n까지의 수를 차례대로
for _ in range(n):
    t = int(input()) # 입력받은 목표 수 t
    
    # 목표 숫자 t가 스택 top에 올 때까지 push
    while next_num <= t:
        stack.append(next_num)
        cmd.append("+")
        next_num += 1
    
    # t와 일치하는 값이 스택의 top이라면 pop
    if stack[-1] == t:
        stack.pop()
        cmd.append("-")
    else:
        # 불가능한 경우
        print("NO")
        exit(0)

# 모든 명령을 출력
print("\n".join(cmd))