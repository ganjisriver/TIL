dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = [[0]*N for _ in range(N)]
    arr[N//2-1][N//2-1], arr[N//2][N//2] = 2, 2
    arr[N//2-1][N//2], arr[N//2][N//2-1] = 1, 1
    for i in range(M):
        x, y, c = map(int, input().split())
        x = x-1
        y = y-1
        arr[x][y] = c
        for j in range(8):
            X = x + dx[j]
            Y = y + dy[j]
            change = []
            while True:
                if X < 0 or Y < 0 or X >= N or Y >= N or arr[X][Y] == 0:
                    change = []
                    break
                elif arr[X][Y] == c:
                    break
                else:
                    change.append((X,Y))
                X, Y  = X+dx[j], Y+dy[j]
            for rx, ry in change:
                arr[rx][ry] = c

    white = 0
    black = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                black += 1
            elif arr[i][j] == 2:
                white += 1
    print(f'#{tc} {black} {white}')


