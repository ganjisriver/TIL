TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    red_matrix = [[0] * 10 for _ in range(10)]
    blue_matrix = [[0] * 10 for _ in range(10)]
    value_list = [list(map(int, input().split())) for _ in range(N)]
    puple_cnt = 0
    for i in range(len(value_list)):
        if value_list[i][4] == 1:
            for j in range(value_list[i][0], value_list[i][2]+1):
                for k in range(value_list[i][1], value_list[i][3]+1):
                    red_matrix[j][k] = 1
        elif value_list[i][4] == 2:
            for j in range(value_list[i][0], value_list[i][2]+1):
                for k in range(value_list[i][1], value_list[i][3]+1):
                    blue_matrix[j][k] = 1

    for r in range(10):
        for c in range(10):
            if red_matrix[r][c] == 1 and blue_matrix[r][c] == 1:
                puple_cnt += 1

    print(f'#{tc} {puple_cnt}')








