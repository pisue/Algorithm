"""
- 문제풀이
1. 문자열 str1과 str2의 길이는 같다
2. 1->2 순서로 번갈아가며 문자열을 하나씩 만든다
3. for문으로 진행
"""

def solution(str1, str2):
    answer = ''
    for i in range(len(str1)):
        answer += str1[i]+str2[i]
    return answer