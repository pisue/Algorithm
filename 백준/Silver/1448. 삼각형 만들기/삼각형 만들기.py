import sys
input = sys.stdin.readline
n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort(reverse=True)

for i in range(n-2):
    if nums[i] < nums[i + 1]+nums[i + 2]:
        print(nums[i]+nums[i + 1]+nums[i + 2])
        sys.exit()
print(-1)
         