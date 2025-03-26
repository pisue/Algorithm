n, m = map(int, input().split())

set_result = float('inf')  # 세트 가격의 최솟값
each_result = float('inf')  # 낱개 가격의 최솟값

for _ in range(m):
    a, b = map(int, input().split())

    # 최소 세트 가격과 최소 낱개 가격 갱신
    set_result = min(set_result, a)
    each_result = min(each_result, b)

# 1. (세트만 구매) 필요한 개수보다 많이 사지만, 전부 세트로 구매
all_set_result = ((n // 6) + 1) * set_result  

# 2. (세트 + 낱개) 세트로 사고 남은 건 낱개로 구매
mix_result = (n // 6) * set_result + (n % 6) * each_result  

# 3. (낱개만 구매) 모든 개수를 낱개로만 구매
all_each_result = n * each_result  

# 최소 비용 계산
print(min(all_set_result, mix_result, all_each_result))
