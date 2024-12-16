"""
- 문제풀이
1. 입력받은 값을 list에 담는다
2. 이 값을 오름차순과 내림차순으로 변수에 담고
3. 입력받은 값의 list와 비교한다
"""
numbers = list(map(int, input().split()))

if sorted(numbers) == numbers:
    print("ascending")
elif sorted(numbers, reverse=True) == numbers:
    print("descending")
else:
    print("mixed")


