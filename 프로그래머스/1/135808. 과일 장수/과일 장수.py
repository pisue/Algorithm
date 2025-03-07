def solution(k, m, score):
    answer = 0
    box_cnt = len(score) // m
    if box_cnt == 0:
        return answer
    score.sort(reverse=True)
    for i in range(box_cnt):
        start_index = m * i
        p = min(score[start_index:start_index+m])
        answer += p * m
    return answer