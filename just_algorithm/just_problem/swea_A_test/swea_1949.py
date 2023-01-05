# visited를 재귀에 넣어주지 않아서, 답이 1씩 오차가 나는 테스트케이스가 발생함.
# 재귀에서 visited의 id 값이 겹치는 것을 방지하기 위해서 visited = set(visited)를 통해 visited의 아이디값을 새로 만들어줌.

from collections import deque


def counting(x, y, value, chance, length, visited):
    global answer
    visited = set(visited)
    visited.add((x, y))

    if answer < length:
        answer = length

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx > N-1 or ny < 0 or ny > N-1 or (nx, ny) in visited:
            continue
        new_value = MAPS[nx][ny]

        if chance == 1:
            if new_value < value:
                counting(nx, ny, new_value, chance, length+1, visited)
            for k in range(K, 0, -1):
                if new_value - k < value:
                    counting(nx, ny, new_value - k, 0, length+1, visited)

        else:
            if new_value < value:
                counting(nx, ny, new_value, 0, length+1, visited)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    answer = 0
    N, K = map(int, input().split())
    MAPS = [list(map(int, input().split())) for _ in range(N)]
    max_height = 0
    starting_point = []
    for i in range(N):
        for j in range(N):
            if MAPS[i][j] > max_height:
                max_height = MAPS[i][j]
    for i in range(N):
        for j in range(N):
            if max_height == MAPS[i][j]:
                starting_point.append((i, j))
    for i in range(len(starting_point)):
        x = starting_point[i][0]
        y = starting_point[i][1]
        counting(x, y, max_height, 1, 1, set())

    print(f'#{tc} {answer}')
