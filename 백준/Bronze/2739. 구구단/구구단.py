"""
- 문제풀이
1. n을 입력받은 뒤 구구단 N단을 출력하는 프로그램을 작성하시오
2. 반복문의 range는 9번으로 고정되어있다
3. print의 형식만 잘맞춰주면 될것같다
"""

n = int(input())

for i in range(1,10):
    print(f"{n} * {i} = {n*i}")