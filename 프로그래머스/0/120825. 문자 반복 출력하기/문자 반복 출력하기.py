"""
문제풀이
1. 제한사항 확인 my_string의 길이는 2보다 같거나 크고 5보다 같거나 작다 
    / 정수 n은 2보다 같거나 크고 10보다 작거나 같다
    / my_string은 영어 대소문자로 이루어져 있습니다
2. string을 for문으로 char를 하나씩 꺼내 정수 n개 만큼 곱하여 answer에 추가한다
3. for문이 끝나면 answer을 리턴한다
"""
def solution(my_string, n):
    answer = ''
    for char in my_string:
        answer += char*n
    return answer