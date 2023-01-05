from collections import deque
def find():
    INF = 987654321
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    dist = [[INF]*N for _ in range(N)]
    dist[0][0] = 0
    q = deque()
    q.append((0, 0))
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                diff = 0
                if MAPS[nr][nc] > MAPS[r][c]:
                    diff = MAPS[nr][nc] - MAPS[r][c]

                if dist[nr][nc] > dist[r][c] + diff + 1:
                    dist[nr][nc] = dist[r][c] + diff + 1
                    q.append((nr, nc))

    return dist[N-1][N-1]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    MAPS = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc} {find()}')
