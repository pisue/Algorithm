while True:
    default_width = 2
    nums = []
    n = int(input())
    if n == 0:
        break;
    for char in str(n):
        nums.append(int(char))
    one = nums.count(1)
    zero = nums.count(0)
    left_num = len(nums) - one - zero
    calc_width = zero*4 + one*2 + left_num*3 + len(nums)-1
    print(default_width + calc_width)
    