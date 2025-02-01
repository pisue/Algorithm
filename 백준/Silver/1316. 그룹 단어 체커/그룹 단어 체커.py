n = int(input())
result = 0

for _ in range(n):
    alph_list = []
    word = input()
    current_alph = ""
    
    # 단어가 한 글자인 경우 자동으로 그룹 단어
    if len(word) == 1:
        result += 1
        continue
        
    is_group_word = True  # 그룹 단어 여부 플래그

    for char in word:
        if current_alph != char and char in alph_list:
            is_group_word = False  # 그룹 단어가 아님
            break
        elif current_alph != char:
            alph_list.append(char)
            current_alph = char

    if is_group_word:
        result += 1

print(result)
        
    
    