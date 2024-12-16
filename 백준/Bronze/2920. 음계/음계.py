"""
- 문제풀이
1. 입력받은 값을 list에 담는다
2. 이 값을 오름차순과 내림차순으로 변수에 담고
3. 입력받은 값의 list와 비교한다
"""
# 입력 받기
numbers = list(map(int, input().split()))

# 오름차순 정렬
ascending = sorted(numbers)

# 내림차순 정렬
descending = sorted(numbers, reverse=True)

# 둘다 아니면 mixed

if ascending == numbers:
    print("ascending")
elif descending == numbers:
    print("descending")
else:
    print("mixed")


