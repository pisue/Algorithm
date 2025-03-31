n = int(input())
left_taller = list(map(int, input().split()))
line = [0] * n
for i in range(1, n+1):
    count = 0
    for j in range(n):
        if line[j] == 0:
            if count == left_taller[i-1]:
                line[j] = i
                break
            count += 1

print(*line)