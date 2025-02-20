import sys

input = sys.stdin.readline

def my_round(val):
    # 소수점 이하가 0.5 이상이면 올림, 그렇지 않으면 내림 (사사오입 방식)
    if val - int(val) >= 0.5:
        return int(val) + 1
    else:
        return int(val)

n = int(input().strip())
if n == 0:
    print(0)
else:
    scores = [int(input().strip()) for _ in range(n)]
    scores.sort()

    # 위, 아래에서 제외할 사람의 수는 n*0.15를 사사오입으로 반올림한 값
    cut = my_round(n * 0.15)
    trimmed_scores = scores[cut:n - cut]

    # 만약 절삭 후 남은 의견이 없다면 0을 출력
    if not trimmed_scores:
        print(0)
    else:
        avg = sum(trimmed_scores) / len(trimmed_scores)
        print(my_round(avg))
