"""
- 문제풀이
1. n의 정수값을 받는다
2. n개의 명령이 주어진다 단, push는 입력할 숫자가 주어진다
3. stack을 선언한다
4. 입력받은 명령대로 실행한다
"""
import sys
input = sys.stdin.read

n, *commands = input().splitlines()
n = int(n)
stack = []

result = []
for command in commands:
    if command.startswith('push'):
        _, b = command.split()
        stack.append(int(b))
    elif command == 'size':
        result.append(len(stack))
    elif command == 'empty':
        result.append(1 if len(stack) == 0 else 0)
    elif command == 'pop':
        result.append(-1 if len(stack) == 0 else stack.pop())
    elif command == 'top':
        result.append(-1 if len(stack) == 0 else stack[-1])

# 출력 한 번에 처리
sys.stdout.write("\n".join(map(str, result)) + "\n")
