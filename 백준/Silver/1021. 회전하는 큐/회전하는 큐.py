from collections import deque

n, m = map(int, input().split())
targets = list(map(int, input().split()))

queue = deque(range(1, n+1))
count = 0

for target in targets:
    idx = queue.index(target)
    
    # 왼쪽으로 회전할지 오른쪽으로 회전할지 결정
    if idx <= len(queue) // 2:
        # 왼쪽으로 회전
        queue.rotate(-idx)
        count += idx
    else:
        # 오른쪽으로 회전
        queue.rotate(len(queue) - idx)
        count += len(queue) - idx
    # 맨 앞의 숫자를 제거
    queue.popleft()
    
print(count)