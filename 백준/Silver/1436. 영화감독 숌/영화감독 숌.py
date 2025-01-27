"""
브루트 포스(Brute Force) 방법을 사용
예) 4자리 숫자로 이루어진 비밀번호를 찾는 경우 0000 -> 9999까지 모든 수를 입력하여 비밀번호를 찾는 것
"""
n = int(input())
cnt = 0
result = 666

while True:
    if '666' in str(result):
        cnt += 1
    if cnt == n:
        break
    
    result += 1
    
print(result)
    