"""
- 문제풀이
1. n : 입력받을 회원의 수
2. 각 회원의 나이와 가입순서 이름을 저장할 members 빈 리스트를 선언한다
3. n의 range만큼 for을 반복한다
4. member를 sort하는데 key = lambda로 나이, 가입순서 순으로 정렬한다
5. member의 나이와 이름을 출력한다
"""
n = int(input())
members = []

for i in range(n):
    age, name = input().split()
    members.append((int(age), i, name))

members.sort(key=lambda x: (x[0], x[1]))

for member in members:
    print(member[0], member[2])