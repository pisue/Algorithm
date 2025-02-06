def solution(s):
    answer = 0
    x = ""
    x_same = 0
    x_not_same = 0
    for i in range(len(s)):
        if x == "": # 첫 글자이거나 분리된 후 첫글자
            x = s[i]
            x_same += 1
        elif x == s[i]: # 첫 글자와 같을 때
            x_same += 1
        else: # 첫 글자와 같이 않을 때
            x_not_same += 1
        
        if x_same == x_not_same: # 첫 글자의 수와 그렇지 않는 수가 같을 때
            answer += 1
            x = ""
            x_same = 0
            x_not_same = 0
            
    if x_same != x_not_same : # 두 횟수가 다른 상태에서 더이상 읽을 글자가 없을 때
        answer += 1
    return answer