n, m = map(int, input().split())
castle = [input() for _ in range(n)]

row_need = 0
for i in range(n):
    if 'X' not in castle[i]:
        row_need += 1
        
col_need = 0

for j in range(m):
     if 'X' not in [castle[i][j] for i in range(n)]:
        col_need += 1

print(max(row_need, col_need))