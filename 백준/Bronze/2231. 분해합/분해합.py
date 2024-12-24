"""
- 문제풀이
1. 자연수 n의 값을 변수에 담는다
2. 1부터 n까지 for문을 통해 하나씩 값을 더해본다
3. 만약 n의 값과 각 분해합이 같을경우 i를 print해준다
4. 3번의 경우가 없으면(즉 i가 n과 같으면) 0을 리턴해준다
"""
n = int(input())

m = 0
for i in range(1, n+1):
    numbers = list(map(int, str(i)))
    m = sum(numbers) + i
    if m == n:
        print(i)
        break
    if i == n:
        print(0)
              