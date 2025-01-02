"""
- 문제풀이
주어진 알파벳이 N 또는 n 이면 "Naver D2", 아니라면 "Naver Whale"을 따옴표를 제외하고 출력한다.
"""

alp = input()

if alp == 'n' or alp == 'N':
    print("Naver D2")
else:
    print("Naver Whale")