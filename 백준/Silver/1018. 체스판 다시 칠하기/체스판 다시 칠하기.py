n, m = map(int, input().split())
board = []

for _ in range(n):
    board.append(input())

result = []

for i in range(n-7):
    for j in range(m-7):
        draw1 = 0  # 'B'로 시작하는 경우
        draw2 = 0  # 'W'로 시작하는 경우
        
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:  
                    if board[a][b] != 'B':
                        draw1 += 1
                    if board[a][b] != 'W':
                        draw2 += 1
                else:
                    if board[a][b] != 'W':
                        draw1 += 1
                    if board[a][b] != 'B':
                        draw2 += 1
        
        # 8x8을 다 검사한 후, 최종 count 추가
        result.append(draw1)
        result.append(draw2)

print(min(result))
