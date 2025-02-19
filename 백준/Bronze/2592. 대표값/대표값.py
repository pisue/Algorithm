n_cnt = [0]*101
nums = []

for _ in range(10):
    n = int(input())
    idx = n//10
    n_cnt[idx] += 1
    nums.append(n)
    
print(sum(nums)//len(nums))
print(n_cnt.index(max(n_cnt))*10)