from collections import deque
def find():
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    # dist = [[INF]*N for _ in range(N)]
    dist[0][0] = MAPS[0][0]
    q = deque()
    q.append((0, 0))
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if dist[nr][nc] > dist[r][c] + MAPS[nr][nc]:
                    dist[nr][nc] = dist[r][c] + MAPS[nr][nc]
                    q.append((nr, nc))

    return dist[N-1][N-1]

tc = 0
while True:
    N = int(input())
    if N == 0:
        break
    MAPS = [list(map(int, input().split())) for _ in range(N)]
    INF = 987654321
    dist = [[INF] * N for _ in range(N)]
    ans = find()
    tc += 1
    print(f'Problem {tc}: {ans}')

