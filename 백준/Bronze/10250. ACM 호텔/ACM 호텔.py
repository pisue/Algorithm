"""
- 문제풀이
1. 테스트 갯수 t의 값을 받는다
2. 층수 :H, 층의 방수:W, 몇번째 손님: N
3. 만약 n을 h로 나눈 나머지가 0이면 최고층수이기 때문에 호수의 앞자리는 h, 뒷자리는 n을 h로 나눈 값이 된다
4. 만약 n을 h로 나눈 나머지가 0이 아니라면 호수의 앞자리는 n을 h로 나눈 나머지, 뒷자리는 n을 h로 나눈 값에 1을 더한다
5. 마지막으로 호수를 구하기 위해 h에 100을 곱한 값에 뒷자리를 더하면 n번째 사람의 호수가 정해진다
"""

t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    if n%h == 0:
        first_num = h
        last_num = n//h
    else:
        first_num = n%h
        last_num = (n//h)+1
    print((first_num*100)+last_num)
