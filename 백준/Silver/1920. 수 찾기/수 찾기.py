"""
- 문제풀이
1. n, m은 다음 줄에 주어지는 정수의 수이다
2. 각 주어지는 수들을 리스트에 담는다 nArr, mArr
3. m으로 주어진 수를 for문을 통해 nArr에 있는지 확인 한 후
    존재하면1 존재하지 않으면 0을 출력한다
"""
n = int(input())
nArr = set(map(int, input().split()))
m = int(input())
mArr = list(map(int, input().split()))

for arr in mArr:
    print(1 if arr in nArr else 0)