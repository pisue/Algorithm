"""
- 문제풀이
1. n은 3의 배수이거나, 5의 배수인지 확인 후 아니면 -1 을 출력
2. for문으로 5를 가장많이 나눌수있는 경우부터 나눈다 -> 봉지를 최소한을 쓰기 위함
3. 나머지를 3으로 나눴을 때 그 나머지가 0일경우는 for의 i값과 3으로 나눈 값을 더하여 return
4. for문이 끝나도 위의 경우가 없을 때 -1 을 리턴
"""

def sugar_delivery(N):
    for i in range(N // 5, -1, -1):
        remaining = N - (i*5)
        if remaining % 3 == 0:
            return i + (remaining // 3)
    return -1

N = int(input())
print(sugar_delivery(N))