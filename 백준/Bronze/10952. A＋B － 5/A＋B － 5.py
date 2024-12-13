"""
- 문제풀이
1. 입력의 마지막이 0 두개가 들어오기 전까지 반복적으로 A+B가 실행되어야한다
2. 재귀함수를 사용해볼까?
3. 파이썬에서는 논리형의 반대를 !를 사용하지않고 not키워드를 사용한다
4. 파이썬에서는 true -> True / false -> False로 사용해야한다
"""

def zero_chk(a, b):
    # a와 b가 모두 0일 경우 True 반환
    return a == 0 and b == 0

while True:
    a, b = map(int, input().split())
    if zero_chk(a, b):
        break
    print(a + b)