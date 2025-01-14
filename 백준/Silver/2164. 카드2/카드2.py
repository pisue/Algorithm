from collections import deque

# 정수 값 받기
n = int(input())
queue = deque(range(1, n + 1))  # 1부터 n까지 초기화

chk = 0
while len(queue) > 1:
    if chk == 0:
        queue.popleft()  # 맨 앞의 값을 제거
        chk = 1
    else:
        a = queue.popleft()  # 맨 앞의 값을 꺼냄
        queue.append(a)     # 꺼낸 값을 다시 맨 뒤에 추가
        chk = 0

print(queue[0])  # 큐에 남은 마지막 값 출력
