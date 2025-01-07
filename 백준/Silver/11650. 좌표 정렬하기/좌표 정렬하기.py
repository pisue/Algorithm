"""
- 문제풀이
1. n개의 점의 값을 받는다
2. coordis 리스트를 선언한다
3. range n의 값만큼 반복하고 받은 값을 coordi에 담는다
4. sort lambda를 사용하여 정렬한다
5. coordis에서 좌표를 꺼내 담는다
"""
n = int(input())

coordis = []

for _ in range(n):
    x, y = input().split()
    coordis.append((int(x), int(y)))

coordis.sort(key=lambda x: (x[0],x[1]))

for coordi in coordis:
    print(coordi[0], coordi[1])