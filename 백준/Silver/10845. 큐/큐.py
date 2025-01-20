from collections import deque
import sys

input = sys.stdin.readline
n = int(input().strip())
queue = deque()

for _ in range(n):
    command = input().strip()
    
    if command.startswith('push'):
        _, value = command.split()  # push와 숫자를 분리
        queue.append(int(value))
    
    elif command == 'pop':
        print(queue.popleft() if queue else -1)
    
    elif command == 'size':
        print(len(queue))
    
    elif command == 'empty':
        print(1 if not queue else 0)
    
    elif command == 'front':
        print(queue[0] if queue else -1)
    
    elif command == 'back':
        print(queue[-1] if queue else -1)
    