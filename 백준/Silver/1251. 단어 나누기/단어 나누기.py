input_str = input()
words = []

for i in range(len(input_str)-2):
    for j in range(i+1, len(input_str)-1):
        str_1 = ''.join(reversed(input_str[0:i+1]))
        str_2 = ''.join(reversed(input_str[i+1:j+1]))
        str_3 = ''.join(reversed(input_str[j+1:]))
        words.append(str_1 + str_2 + str_3)
        
words.sort()
print(words[0])
       
    
