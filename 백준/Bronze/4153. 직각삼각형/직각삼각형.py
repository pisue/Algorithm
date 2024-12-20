"""
입력은 여러개의 테스트케이스로 주어지며 마지막줄에는 0 0 0이 입력된다.
- 문제풀이
1. 주어진 세개의 수를 리스트에 담든다
2. 가장 길이가 긴 수를 찾아 변수에 담는다
3. numbers에서 max값이 아닌것을 새로운 배열에 담는다
3. 가장긴 수의 길이의 제곱과 나머지 두 수의 제곱의 합이 같다면 right를 출력
4. 그렇지 않다면 wrong을 출력
"""
numbers = list(map(int, input().split()))
while sum(numbers) > 0:
    max_num = max(numbers)
    left_numbers = []

    for num in numbers:
        if max_num != num:
            left_numbers.append(num)

    if max_num**2 == sum(num**2 for num in left_numbers):
        print("right")
    else:
        print("wrong")
    
    numbers = list(map(int, input().split()))
