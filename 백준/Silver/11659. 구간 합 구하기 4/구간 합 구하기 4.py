import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))
sum_num = [0]
this_sum = 0

for num in nums:
    this_sum += num
    sum_num.append(this_sum)
    
for _ in range(m):
    i, j = map(int, input().split())
    print(sum_num[j] - sum_num[i-1])