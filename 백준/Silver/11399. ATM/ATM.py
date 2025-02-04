n = int(input())
p_list = list(map(int, input().split()))
p_list.sort()
t = 0
answer = 0
for p in p_list:
    t += p
    answer += t
print(answer)