"""
- 문제풀이
1. 기존의 A+B문제처럼 기준점이 있지 않다
2. 그럼 입력이 되지 않을 때 exception이 발생하는데 python은 try-except를 사용하면된다
"""
while True:
    try:
        a, b = map(int, input().split())
    except:
        break
    print(a+b)