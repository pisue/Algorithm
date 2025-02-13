n = int(input())
rank = [1] * n
weight = []
height = []
for _ in range(n):
    w, h = map(int, input().split())
    weight.append(w)
    height.append(h)

for i in range(n-1):
    for j in range(i+1, n):
        if weight[i] > weight[j] and height[i] > height[j]:
            rank[j] += 1
        elif weight[j] > weight[i] and height[j] > height[i]:
            rank[i] += 1
print(*rank)