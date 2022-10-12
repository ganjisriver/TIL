from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def ladder(x, y, life):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if examinant[nx][ny] != 444 and examinant[nx][ny] != -1 and life > examinant[nx][ny]:
            examinant[nx][ny] = life
        else:
            continue


T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    examinant = [[0]*(M+K*2) for _ in range(N+K*2)]
    first_cell = [list(map(int, input().split())) for _ in range(N)]
    disabled_cells = deque()
    active_cells = deque()
    dead_cell = set()
    DEAD = 444
    for i in range(N):
        for j in range(M):
            cell = first_cell[i][j]
            if cell:
                examinant[i+K][j+K] = cell
                life = cell
                disabled_cells.append((i+K, j+K, life, cell))

    while K+1:
        for i in range(len(disabled_cells)):
            x, y, left_life, life = disabled_cells.popleft()
            if left_life == 0:
                active_cells.append((x, y, life))
            else:
                disabled_cells.append((x, y, left_life-1, life))

        if K == 0:
            break

        if active_cells:
            for i in range(len(active_cells)):
                x, y, life = active_cells.popleft()










