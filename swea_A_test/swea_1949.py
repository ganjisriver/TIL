def counting(x, y):
    global chance, cnt, K

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if chance and mountain[nx][ny] - K < mountain[x][y] <= mountain[nx][ny]:
                chance = 0
                cnt = cnt + 1
                counting(nx, ny)
            elif not chance and mountain[x][y] > mountain[nx][ny]:
                cnt = cnt +1
                counting(nx, ny)



dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split()))]
    top_value = 0
    mountain_top = []
    chance = 1
    cnt = 1
    for i in range(N):
        for j in range(N):
            if top_value < mountain[i][j]:
                top_value = mountain[i][j]

    for r in range(N):
        for c in range(N):
            if mountain[r][c] == top_value:
                mountain_top.append((r, c))

    for i in range(len(mountain_top)):
        counting(mountain_top[i][0], mountain_top[i][1])
