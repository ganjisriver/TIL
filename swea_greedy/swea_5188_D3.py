def counting(x, y, total):
    global min_value
    if x == N-1 and y == N-1 and min_value > total:
        min_value = total
        return
    if total > min_value:
        return
    for i in range(2):
        nx = x + index[i][0]
        ny = y + index[i][1]
        if 0 <= nx < N and 0 <= ny < N:
            # total += arr[nx][ny]
            counting(nx, ny, total+arr[nx][ny])

index = [(1, 0), (0, 1)]

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    r, c = 0, 0
    min_value = 1000000001
    counting(r, c, arr[0][0])
    print(f'#{tc} {min_value}')
