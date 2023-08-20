from collections import deque
N, M, T = map(int, input().split())
table = []

for i in range(N):
    circle = deque(list(map(int, input().split())))
    table.append(circle)

for i in range(T):
    x, d, k = map(int, input().split())

    cnt = x
    rotate_cnt = k % N

    # 돌려돌려 돌림판
    while cnt <= N:
        if d == 0:
            for j in range(rotate_cnt):
                right = table[cnt-1].pop()
                table[cnt-1].appendleft(right)
        else:
            for j in range(rotate_cnt):
                left = table[cnt-1].popleft()
                table[cnt-1].append()

    # 인접 제거
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for j in range(N):
        for k in range(M):
            if table[j][k] == 'x':
                continue
            visited = set()
            queue = deque([j, k, table[j][k]])
            current = queue.popleft()
            visited.add((current))
            for l in range(4):
                dr = j + direction[l][0]
                dc = k + direction[l][1]
                if 0 <= dr < N:
                    if dc == -1:
                        dc = (N-1)
                    elif dc == N:
                        dc = 0
                    if current[2] == table[dr][dc]:
                        continue
                else:
                    continue