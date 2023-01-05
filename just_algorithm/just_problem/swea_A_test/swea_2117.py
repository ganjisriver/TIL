dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(visit, k):
    next_visited = set()
    visit = set(visit)
    if k == end:
        return
    while visit:
        x, y = visit.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y = dy[i]
            if nx < 0 or nx > N-1 or ny < 0 or ny > N-1 or (nx, ny) in visit:
                continue
            next_visited.add((nx, ny))
            visited.add((nx,ny))
    bfs(next_visited, k+1)


def calculation():
    global earning
    cnt = 0
    for x, y in visited:
        if area[x][y] == 1:
            cnt += 1
    this_earning = (cost*cnt) - (end)*(end) + ((end-1)*(end-1))
    if this_earning > earning:
        earning = this_earning


T = int(input())
for tc in range(1, T+1):
    N, cost = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(N)]
    earning = 0
    for i in range(N):
        for j in range(N):
            for end in range(1, N+1):
                visited = set()
                visited.add((i, j))
                bfs(visited, 1)
                calculation()
    print(f'#{tc} {earning}')

