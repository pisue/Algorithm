import sys
input = sys.stdin.readline

#계수정렬
n = int(input())
numbers = [0] * (10000 + 1)

#각 입력값에 해당하는 인덱스의 값 +1
for _ in range(n):
    numbers[int(input())] += 1
  
#numbers 기록된 정보 확인
for i in range(len(numbers)):
    if numbers[i] != 0: #0이 아닌 데이터가 기록된 데이터
        for _ in range(numbers[i]):
            print(i)
