def bfs(visited, current, cnt, used):
    global min_cnt
    if min_cnt < cnt:
        return
    if current == exit_position:
        if cnt < min_cnt:
            min_cnt = cnt
        return
    for i in range(4):
        dr = current[0] + direction[i][0]
        dc = current[1] + direction[i][1]
        if 0 <= dr < N and 0 <= dc < M:
            if (dr, dc) not in visited:
                if miro[dr][dc]:
                    if used:
                        return
                    else:
                        used = True
                        visited.add((dr, dc))
                        bfs(visited, (dr, dc), cnt+1, used)
                else:
                    visited.add((dr, dc))
                    bfs(visited, (dr, dc), cnt+1, used)
            else:
                return








direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
N, M = map(int, input().split())
current = tuple(map(int, input().split()))
exit_position = tuple(map(int, input().split()))
miro = []
min_cnt = 999999999999999
for i in range(N):
    miro.append(list(map(int, input().split())))

current = (current[0]-1, current[1]-1)
exit_position = (exit_position[0]-1, exit_position[1]-1)
bfs(set(current), current, 0, 0)
print(min_cnt)

