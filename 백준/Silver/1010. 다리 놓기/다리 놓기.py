import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    result = 1
    for i in range(n):
        result *= (m-i)
        result //= (i+1)
    print(result)