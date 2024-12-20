"""
- 문제풀이
1. 첫 줄에 참가자의 수 N이 주어짐
2. 둘째줄에 티셔츠 사이즈별 신청자의 수 S, M, L, XL, XXL, XXXL이 공백으로 구분
3. 셋째 줄에 정수 티셔츠와 펜의 묶음 수를 의미하는 T와 P가 공백으로 구분되어 주어집니다
4. 티셔츠는 T장 묶음으로만 주문할 수 있다
5. 펜은 P자루씩 묶음 혹은 한자루씩 주문할 수 있음
---
- 출력
1. 첫줄에 티셔츠를 T장씩 몇 묶음 주문해야 하는가
2. for문으로 각 숫자를 T로 나눈 나머지가 0이면 몫을 결과값에 +=해주고
    0이 아니면 몫+1을 한값을 += 해준다
3. 두번째 줄은 n//p, n%p의 값을 출력해준다
"""
n = int(input())
numbers = list(map(int, input().split()))
t, p = map(int, input().split())

t_total = 0
for num in numbers:
    t_total += num//t if num%t == 0 else (num//t+1)
print(t_total)
print(n//p, n%p)