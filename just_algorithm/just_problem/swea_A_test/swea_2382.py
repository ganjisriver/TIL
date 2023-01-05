from collections import deque

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]
transition = {1:2, 2:1, 3:4, 4:3}
T = int(input())
for tc in range(1, T+1):
    N, time, K = map(int, input().split())
    arr = [[[]]*N for _ in range(N)]
    current_idx = deque()
    for _ in range(K):
        sell = list(map(int, input().split()))
        x = sell[0]
        y = sell[1]
        amount = sell[2]
        direction = sell[3]
        current_idx.append((x, y, sell[2], sell[3]))
        # arr[x][y] = [(x, y, sell[2], sell[3])]

    chance = 0
    while chance < time:
        for i in range(len(current_idx)):
            x, y, amount, direction = current_idx.popleft()

            nx = x + dx[direction]
            ny = y + dy[direction]
            if nx == 0 or nx == N-1 or ny == 0 or ny == N-1:
                current_idx.append((nx, ny, amount//2, transition[direction]))
                # arr[nx][ny].append((nx, ny, amount//2, transition[direction]))
            else:
                current_idx.append((nx, ny, amount, direction))
        s = len(current_idx)
        for i in range(s):
            for j in range(i+1, s-1):
            if current_idx[i][0]:








    print(arr[0][0])
    print(len(arr[0][0]))
