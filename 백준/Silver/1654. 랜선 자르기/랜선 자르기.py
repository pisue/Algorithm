"""
- 이진 탐색을 사용한 해결
"""

k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]

left, right = 1, max(lines) # 탐색 범위 설정
answer = 0

while left <= right:
    # 중간값(랜선의 길이)
    mid = (left + right) // 2 
    # 만들 수 있는 랜선 개수 계산
    count = sum(length // mid for length in lines)
    if count >= n: # n개 이상 만들 수 있는 경우
        answer = mid # 가능한 길이 후보 저장
        left = mid + 1 # 더 긴 길이를 시도
    else:
        right = mid -1 # 더 짧은 길이를 시도

print(answer)
    
        