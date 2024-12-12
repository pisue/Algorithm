"""
문제풀이_1
1. my_string의 인덱스부터 overwrite_string의 길이만큼을 overwrite_string으로 대체
2. my_string의 인덱스 기준점 앞과 overwrite_string의 길이 뒤 인덱스를 두개의 변수로 나눈다
3. my_string_1, overwrite_string, my_string_2를 합쳐 print한다
문제풀이_2
1. re.sub을 사용해볼까? re.sub(찾을 패턴, 대체할 문자, 찾을 문자열)
2. 찾을 패턴 -> my_string에서 인덱스 s부터 s에 overwrite_string의 길이를 더한만큼 sub()해준다
3. 대체할 문자에 overwrite_string을 넣는다
4. 찾을 문자열에 my_string을 입력한다
"""
import re
def solution(my_string, overwrite_string, s):
    return my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]

    
     