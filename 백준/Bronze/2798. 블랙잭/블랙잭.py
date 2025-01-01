"""
- 문제풀이 (답을 확인한 후 푼 문제)
1. for문 중첩을 이용한 풀이
2. n과 m의 값을 받는다
3. 입력된 숫자들을 리스트로 받는다
4. add_list 초기 선언한다
5. 1_for n의 range 만큼 복한다
6. 2_for i+1부터 N의 range만큼 반복한다
7. 3_for j+1부터 N의 range만큼 반복한다
8. list의 i, j, k의 값을 더했을 때 M보다 작을 경유 add_list에 담는다
9. M보다 클 경우 continue
10. print(max(add_list))
"""

n, m = map(int, input().split())
lst = list(map(int, input().split()))
add_list = []

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            add_num = lst[i] + lst[j] + lst[k]
            if add_num > m:
                continue
            else:
                add_list.append(add_num)
print(max(add_list))