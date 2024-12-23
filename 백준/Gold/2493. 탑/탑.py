"""
- 문제풀이2
1. 이중 for문으로 풀었을 때 시간 초과
2. stack의 개념적 이해와 이 문제를 접근하는 사고가 중요함
3. 이 문제는 내가 풀었다고 할 수 없음
4. 참고해서 푼 문제이고 다음에 꼭 다시 풀어봐야 할 문제임
"""

n = int(input())
heights = list(map(int, input().split()))
result = [0] * n
stack = []

for i in range(n):
    # 현재 탑보다 낮은 탑은 스택에서 제거
    while stack and stack[-1][1] <= heights[i]:
        stack.pop()
    
    # 스택이 비어있지 않다면, 현재 탑을 수신하는 탑의 인덱스 저장
    if stack:
        result[i] = stack[-1][0] + 1
    
    # 현재 탑을 스택에 추가 (인덱스, 높이)
    stack.append((i, heights[i]))

print(" ".join(map(str, result)))