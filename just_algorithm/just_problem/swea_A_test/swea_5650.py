dr = [-1, 1, 0, 0]  # 상 하 좌 우
dc = [0, 0, -1, 1]
block = [[], []]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    game_board = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if game_board[i][j] != 0:
                continue
            
