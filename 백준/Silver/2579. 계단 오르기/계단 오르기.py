n = int(input())

if n == 1:
    print(int(input()))  # n=1이면 바로 출력 후 종료
    exit()

stair = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n+1)

dp[1] = stair[1]
dp[2] = stair[1] + stair[2]

if n > 2:  # n이 3 이상일 때만 dp 계산
    dp[3] = max(stair[1] + stair[3], stair[2] + stair[3])  # dp[3]을 미리 초기화

    for i in range(4, n+1):  # i는 4부터 시작해야 안전함
        dp[i] = max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i])

print(dp[n])
