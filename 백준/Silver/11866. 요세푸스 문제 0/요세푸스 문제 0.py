from collections import deque
n, k = map(int,input().split())
queue = deque(range(1, n + 1)) # 1부터 n까지 큐에 삽입
result = [] # 제거된 순서를 저장할 리스트

while queue:
    queue.rotate(-(k-1))
    result.append(queue.popleft())

print(f"<{', '.join(map(str, result))}>")
