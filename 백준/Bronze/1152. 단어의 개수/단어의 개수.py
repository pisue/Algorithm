"""
- 문제풀이
1. 대소문자 공백으로 이루어진 문자열을 받는다
2. 이를 공백으로 split한 후 list로 만든다
3. 이 리스트의 크기가 단어의 수가 된다
"""

str_list = list(map(str, input().split()))

print(len(str_list))
