import sys
from collections import Counter

input = sys.stdin.readline

# 산술평균 (단, 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.)
def fun1(nums):
    print(round(sum(nums) / len(nums)))
    
# 중앙값
def fun2(nums):
    # 수들을 중가하는 순서대로 나열
    nums.sort()
    print(nums[len(nums) // 2])
    
# 최빈값 (단, 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다)
def fun3(nums):
    cnt = Counter(nums)  # 등장 횟수를 카운트
    max_freq = max(cnt.values())  # 최빈값의 빈도수

    modes = [key for key, val in cnt.items() if val == max_freq]  
    modes.sort()  # 정렬하여 두 번째로 작은 값을 찾을 수 있도록 설정

    if len(modes) > 1:
        print(modes[1])  # 두 번째로 작은 값 출력
    else:
        print(modes[0])  # 하나뿐이면 그대로 출력

# 범위
def fun4(nums):
    print(max(nums)-min(nums))
    
n = int(input())
num_list = [int(input()) for _ in range(n)]

fun1(num_list)
fun2(num_list)
fun3(num_list)
fun4(num_list)
    