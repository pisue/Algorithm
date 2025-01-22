t = int(input())
for _ in range(t):
    k = int(input()) # 층
    n = int(input()) # 호실
    
    # 0층의 초기값 설정
    floor = list(range(1, n+1))
    
    # 1층부터 k층까지 채우기
    for _ in range(k):
        for j in range(1, n):
            floor[j] += floor[j - 1] # 이전 호실과 누적 합
            
    print(floor[-1]) # k층 n호 출력
            
    