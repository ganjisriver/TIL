white_board = [[0]*100 for _ in range(100)]
N = int(input())
for i in range(N):
    x, y = map(int, input().split())
    for j in range(10):
        for k in range(10):
            white_board[x+j-1][y+k-1] = 1
square = 0
for i in range(100):
    for j in range(100):
        if white_board[i][j]:
            square += 1

print(square)
