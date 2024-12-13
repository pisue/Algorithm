"""
- 문제풀이
1. 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 이 값을 먼저받는다
2. 이 케이스 개수만큼 A와 B가 주어진다 (값을 추가로 받는 것)
3. 두 수를 더한 값을 출력한다
"""
t = int(input())

for _ in range(0, t):
    a, b = map(int, input().split())
    print(a+b)