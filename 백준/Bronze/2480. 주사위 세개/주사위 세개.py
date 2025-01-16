numbers = list(map(int, input().split()))

if len(set(numbers)) == 1:  # 세 숫자가 모두 같음
    print(10000 + numbers[0] * 1000)
elif len(set(numbers)) == 2:  # 두 숫자만 같음
    for num in numbers:
        if numbers.count(num) == 2:  # 같은 숫자 찾기
            print(1000 + num * 100)
            break
else:  # 모두 다른 숫자
    print(max(numbers) * 100)