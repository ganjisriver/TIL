"""
서로 연결되지 않은 파이프일 때를 고려 잘 해야됨 + 파이프를 어떤식으로 자료구조할 것인가도 고민해봐야함.
"""
from collections import deque
dr = [-1, 1, 0, 0] # 상 하 좌 우
dc = [0, 0, -1, 1]
pipe_line = [[], [0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]
connection = {0: 1, 1: 0, 2: 3, 3: 2}


def counting(stack, current):
    next_stack = set()
    stack = set(stack)
    if current == time:
        return
    while stack:
        r, c = stack.pop()
        pipe_number = MAPS[r][c]
        for i in pipe_line[pipe_number]:
            nr = r + dr[i]
            nc = c + dc[i]
            if nr > N-1 or nr < 0 or nc > M-1 or nc < 0 or (nr, nc) in visited:
                continue

            if connection[i] in pipe_line[MAPS[nr][nc]]:
                visited.add((nr, nc))
                next_stack.add((nr, nc))
    counting(next_stack, current+1)


T = int(input())
for tc in range(1, T+1):
    N, M, x, y, time = map(int, input().split())
    MAPS = [list(map(int, input().split())) for _ in range(N)]
    visited = {(x, y)}
    counting(visited, 1)
    print(f'#{tc} {len(visited)}')
#
# dr = [-1, 1, 0, 0] # 상 하 좌 우
# dc = [0, 0, -1, 1]
# pipe_line = [[], [0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]
# connection = {0: 1, 1: 0, 2: 3, 3: 2}
#
#
# def counting(r, c, current, pipe_number):
#     visited.add((r, c))
#     if current == time:
#         return
#
#     while q:
#
#     # for i in pipe_line[pipe_number]:
#     #     nr = r + dr[i]
#     #     nc = c + dc[i]
#     #     if nr > N-1 or nr < 0 or nc > M-1 or nc < 0:
#     #         continue
#     #
#     #     if connection[i] in pipe_line[MAPS[nr][nc]]:
#     #         counting(nr, nc, current+1, MAPS[nr][nc])
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M, x, y, time = map(int, input().split())
#     MAPS = [list(map(int, input().split())) for _ in range(N)]
#     visited = set()
#     q = deque()
#     counting(x, y, 1, MAPS[x][y])
#     print(f'#{tc} {len(visited)}')