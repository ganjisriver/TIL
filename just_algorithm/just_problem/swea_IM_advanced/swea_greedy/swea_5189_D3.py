def counting(depth, x):
    global min_value
    if depth == N-1:
        idx[depth] = matrix[x][0]
        if min_value > sum(idx):
            min_value = sum(idx)
        return

    for i in range(2, len(visited)):
        if not visited[i]:
            visited[i] = 1
            idx[depth] = matrix[x][i-1]
            counting(depth + 1, i-1)
            visited[i] = 0

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    min_value = 10000001
    visited = [0] * (N + 1)
    idx = [0] * (N+2)
    visited[1] = 1
    counting(0, 0)
    print(f'#{tc} {min_value}')