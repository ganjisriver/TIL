N, M = map(int, input().split())
board = [input() for _ in range(N)]
cnt = 99999999
for i in range(N-7):
    for j in range(M-7):
        w_cnt = 0
        b_cnt = 0
        for r in range(8):
            for c in range(8):
                if (r+c) % 2 == 0:
                    if board[i+r][j+c] != 'W':
                        w_cnt += 1
                    else:
                        b_cnt += 1
                else:
                    if board[i+r][j+c] != 'W':
                        b_cnt += 1
                    else:
                        w_cnt += 1

        if cnt > min(w_cnt, b_cnt):
            cnt = min(w_cnt, b_cnt)
print(cnt)