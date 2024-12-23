"""
- 문제풀이
1. 입력된 두 값을 변수에 담는다
2. 유클리드 호제법을 사용한다
3. 최소공배수를 구하는 함수를 먼저 구현하고(gcd)
4. gcd를 활용하여 최대공약수를 구하는 함수를 구현한다(lcm)
"""

a, b = map(int, input().split())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a,b))
print(lcm(a,b))