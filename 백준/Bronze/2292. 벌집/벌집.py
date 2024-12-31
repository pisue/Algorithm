"""
- 문제풀이
1. 정수 n을 받는다
2. 육각형이기 때문에 1 -> 6 -> 12... 즉 6의 배수로 숫자가 둘러싼다
3. 초기 방을 선언하고 while이 돌면서 저장 할 현재 방의 번호 변수를 선언한다
3. range_end가 n보다 작을때 까지 반복하며 range_end에 layer에 6을 곱한 값을 더해준다
"""
n = int(input())
layer = 1 # 초기 방 1번
range_end = 1 # 현재 층의 마지막 방 번호

while n > range_end:
    range_end += 6 * layer
    layer += 1
    
print(layer)