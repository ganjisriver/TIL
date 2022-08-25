TC = int(input())
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]
for tc in range(1, TC+1):
    N = int(input())
    matrix = [list(map(int, list(input()))) for _ in range(N)]
    start_r = 0
    start_c = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                start_r = i
                start_c = j

            if matrix[i][j] == 3:
                end_r = i
                end_c = j
    q = [(start_r, start_c)]
    visited = set()
    cnt = 0
    while q:
        r, c = q.pop()
        visited.add((r, c))
        if matrix[r][c] == 3:
            result = (r, c)
            break
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if nr >= N or nr < 0 or nc >= N or nc < 0:
                continue

            if (nr, nc) in visited or matrix[nr][nc] == 1:
                continue
            q.append((nr, nc))
        cnt += 1
        if (start_r, start_c) in visited:
            del (start_r, start_c)
        if matrix[r][c] == 2:
            cnt = 0

    if (end_r, end_c) not in visited:
        cnt = 0
    print(cnt)
