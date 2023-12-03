T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    accumulated_arr = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(M):
        r1, c1, r2, c2, v = map(int, input().split())
        accumulated_arr[r1][c1] += v
        if 0 < r2 < N:
            accumulated_arr[r2+1][c1] -= v
        if 0 < c2 < N:
            accumulated_arr[r1][c2+1] -= v
        # if 0 < r2 < N and 0 < c2 < N:
        #     accumulated_arr[r2+1][c2+1] += v
    for i in range(1, N+1):
        print(accumulated_arr[i][1:])
    # 가로 더하기

    for i in range(1, N+1):
        for j in range(1, N+1):
            accumulated_arr[i][j] += accumulated_arr[i][j-1]
    # 세로 더하기
    for i in range(1, N+1):
        for j in range(1, N+1):
            accumulated_arr[j][i] += accumulated_arr[j][i-1]
    # 누적합이랑 원본배열 더하기
    for i in range(1, N+1):
        for j in range(1, N+1):
            arr[i][j] += accumulated_arr[i][j]
        print(*arr[i][1:])


