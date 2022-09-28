def finding(a, b):
    global cnt
    for k in range(4):
        r = a + dr[k]
        c = b + dc[k]
        if r < 0 or c < 0 or r >= N or c >= N:
            continue
        elif arr[r][c] != arr[a][b]+1:
            continue
        else:
            cnt += 1
            finding(r, c)
            break
        return cnt


dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]
TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 1
    min_result = N * N
    for i in range(N):
        for j in range(N):
            cnt = 1
            finding(i, j)
            if max_cnt < cnt:
                max_cnt = cnt
                result = arr[i][j]
                min_result = result
                if min_result > result:
                    min_result = result
            elif max_cnt == cnt:
                result = arr[i][j]
                if min_result > result:
                    min_result = result
    print(f'#{tc} {min_result} {max_cnt}')

