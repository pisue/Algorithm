import sys
input = sys.stdin.readline
n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

# arr1의 숫자 빈도수를 저장할 딕셔너리 생성
counter = {}

for num in arr1:
    if num in counter:
        counter[num] += 1
    else:
        counter[num] = 1

# arr2의 숫자 빈도 확인
result = [counter.get(num, 0) for num in arr2]

# 출력
print(*result)