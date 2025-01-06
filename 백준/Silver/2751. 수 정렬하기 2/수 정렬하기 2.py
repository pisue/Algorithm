import sys

# 빠른 입출력 사용
input = sys.stdin.read
data = input().split()

# 첫 번째 입력은 숫자의 개수
n = int(data[0])

# 나머지 입력을 정수로 변환
arr = list(map(int, data[1:]))

# 정렬 수행
arr.sort()

# 출력 결과를 한 번에 출력
sys.stdout.write("\n".join(map(str, arr)) + "\n")

