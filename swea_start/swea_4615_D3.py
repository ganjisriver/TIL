def counting(x, y, i):
    if c == 1:
        X = x+dx[i]
        Y = y+dy[i]
        if X < 0 or Y < 0 or X >= N or Y >= N:
            return
        if arr[X][Y] == 2:
            arr[X][Y] = 1
            X += dx[i]
            Y += dy[i]
            if X < 0 or Y < 0 or X >= N or Y >= N:
                return
            if arr[X][Y] == 1:
                return arr
            else:
                X -= dx[i]
                Y -= dy[i]
                counting(x, y, i)
    if c == 2:
        X = x+dx[i]
        Y = y+dy[i]
        if X < 0 or Y < 0 or X >= N or Y >= N:
            return
        if arr[X][Y] == 1:
            arr[X][Y] = 2
            X += dx[i]
            Y += dy[i]
            if X < 0 or Y < 0 or X >= N or Y >= N:
                return
            if arr[X][Y] == 2:
                return arr
            else:
                X -= dx[i]
                Y -= dy[i]
                counting(X, Y, i)



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
            counting(x, y, j)
    print(arr)
    white = 0
    black = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                black += 1
            elif arr[i][j] == 2:
                white += 1
    print(f'#{tc} {black} {white}')


