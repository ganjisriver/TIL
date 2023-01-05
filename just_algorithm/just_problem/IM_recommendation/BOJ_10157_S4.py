dr = [1, 0, -1, 0]  # 하우상좌
dc = [0, 1, 0, -1]

C, R = map(int, input().split())
K = int(input())
# arr = [[0]* for _ in range(C)]

if C*R < K:
    print('0')
elif K == 1:
    print('1 1')

else:
    cnt = 1
    visited = set()
    visited.add((0, 0))
    place = (0, 0)
    direction = 0
    while len(visited) < C*R:
        (x, y) = place
        nx = x + dr[direction]
        ny = y + dc[direction]
        if nx < 0 or nx >= R or ny < 0 or ny >= C or (nx, ny) in visited:
            direction += 1
            direction = (direction % 4)
            continue
        place = (nx, ny)
        visited.add((nx, ny))
        cnt += 1
        if cnt == K:
            print(f'{ny+1} {nx+1}')
            break