word = input().strip()
lower_word = word.lower()
asc = [0] * 26  # 알파벳 개수만큼

for char in lower_word:
    idx = ord(char) - ord('a')  # 'a'를 0번 인덱스로 맞춤
    asc[idx] += 1

max_num = max(asc)
max_cnt = asc.count(max_num)

if max_cnt > 1:
    print("?")
else:
    max_idx = asc.index(max_num)
    print(chr(max_idx + ord('A')))  # 대문자로 변환