t = int(input()) # 테스트 케이스 개수
dp = [0] * 11 # n은 최대 10까지 주어짐

# 초기값 설정
dp[1], dp[2], dp[3] = 1, 2, 4

# DP 테이블 채우기
for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
# 테스트 케이스 실행
for _ in range(t):
    n = int(input())
    print(dp[n])