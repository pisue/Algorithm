"""
- 문제풀이
1. 오른쪽 기준으로 정렬한게 핵심
2. 공백의 갯수와 별의 갯수의 합이 입력받은 n개
3. for문으로 반복하며 공백의 갯수는 하나씩 줄어들고 별의 갯수는 하나씩 늘어나게 print()
"""
n = int(input())
blank = n-1
star = 1
for i in range(n):
    print_balnk = " "*blank
    print_star = "*"*star
    print(f"{print_balnk}{print_star}")
    blank -= 1
    star += 1