"""
- 문제풀이
1. 시간과 분을 값으로 받는다
2. 시간과 분을 계산하여 분으로 바꾼다 그 후 45를 뺀값을 새 변수에 담는다
3. 시간으로 바꿔 프린트 해준다
4. 여기서 0시일 때를 고려하지 못함
"""

h, m = map(int, input().split())

newMinute = ((h*60)+m) - 45

if newMinute < 0:
    newMinute += 24 * 60

h2 = newMinute//60
m2 = newMinute%60

print(h2, m2)
