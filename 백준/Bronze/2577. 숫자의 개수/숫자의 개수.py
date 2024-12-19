"""
- 문제풀이
1. 세개의 자연수 a, b, c를 담는다
2. calc = a*b*c를 계산한다
3. 크기가 10인 arr을 선언한다
4. calc를 str로 바꿔주고 for문을 한글자씩 가져온다
5. 가져온 char를 다시 int로 형변환 한후 선언한 배열의 인덱스를 찾아 +1을 해준다
6. 배열의 값을 하나씩 출력한다
"""

a = int(input())
b = int(input())
c = int(input())

calc = a*b*c
arr = [0]*10

for char in str(calc):
    arr[int(char)] += 1
    
for r in arr:
    print(r)