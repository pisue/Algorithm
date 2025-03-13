import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
count = 0
# 가장 수가 큰 코인부터 선택
coins.sort(reverse = True)

# 적절성 검사 : 만약 선택된 동전의 가치가 남은 돈 보다 크다면 다음 작은 동전을 선택
for coin in coins:
    count += k // coin
    k = k % coin
    if k == 0:
        break
print(count)
