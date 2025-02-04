import sys

# 입력을 한 번에 읽고 줄 단위로 분리
data = sys.stdin.read().splitlines()

# 첫 줄: n(첫 번째 집합 크기), m(두 번째 집합 크기)
n, m = map(int, data[0].split())

# n개의 이름 리스트
n_names = data[1:n+1]

# m개의 이름 리스트
m_names = data[n+1:n+1+m]

# 교집합을 찾기
mn_names = sorted(set(n_names) & set(m_names))  # 두 리스트의 교집합을 정렬

# 결과 출력
print(len(mn_names))
print("\n".join(mn_names))  # 줄바꿈을 이용한 빠른 출력
