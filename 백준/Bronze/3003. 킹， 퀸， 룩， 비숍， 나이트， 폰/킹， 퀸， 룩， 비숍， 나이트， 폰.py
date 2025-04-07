white = list(map(int, input().split()))
option = [1, 1, 2, 2, 2, 8]
result = []
for i in range(len(white)):
    result.append(option[i]-white[i])
    
print(*result)