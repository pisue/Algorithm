nums = [0]*1001
number = 1
count = 0
for i in range(1, 1001):
    nums[i] = number
    count += 1
    if number == count:
        count = 0
        number += 1

a, b = map(int, input().split())
print(sum(nums[a:b+1]))
        
            
    