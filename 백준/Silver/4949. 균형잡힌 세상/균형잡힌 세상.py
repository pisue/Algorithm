while True:
    s = input()
    if s == ".":
        break
    
    stack = []
    is_balanced = True
    
    for char in s:
        if char in "([": # 여는 괄호는 스택에 추가
            stack.append(char)
        elif char in ")]": # 닫는 괄호일 경우
            if not stack: #스택이 비어있으면 짝이 안 맞음
                is_balanced = False
                break
            top = stack.pop()
            if (char == ")" and top != "(") or (char == "]" and top != "["): # 짝이 맞지 않음
                is_balanced = False
                break
    if is_balanced and not stack:
        print("yes")
    else:
        print("no")
           
            
    