n = int(input())

if n == 1:
    print(1)
    exit()
elif n == 2:
    print(2)
    exit()

dp = [0] * (n + 1)
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007  # 모듈러 연산을 미리 적용하여 오버플로우 방지

print(dp[n])

