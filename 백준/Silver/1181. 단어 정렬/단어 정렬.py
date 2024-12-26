"""
- 문제풀이_1 
-> 이 방법 말고 다른 방법으로 풀었음 자세한건 깃헙 커밋 코멘트에 정리하겠음
1. 첫줄에 주어진 숫자를 n에 담는다
2. n개만큼 주어질 단어를 담을 리스트를 선언한다
3. n의 숫자만큼 한줄 씩 단어가 주어진다
4. 길이가 짧은 것부터 정렬
5. 만약 길이가 같으면 사전 순으로 정렬
6. 만약 중복된 단어는 하나만 남기고 제거한다.
"""
n = int(input())
arr = []
for _ in range(n):
    arr.append(input())
    
#set 집합은 순서가 없기 때문에 다시 list로 감싸줘야한다
arr = list(set(arr))
arr.sort(key = lambda s : [len(s), s])
print('\n'.join(arr))