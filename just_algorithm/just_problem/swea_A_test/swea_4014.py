T = int(input())
for tc in range(1, T+1):
    N, length = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    install_number = 0

    #가로
    for i in range(N):
        one_line = board[i]
        can_install = True
        installing = False
        cnt = 1
        for j in range(N-1):
            if one_line[j] == one_line[j+1]:
                cnt += 1
                if installing and (cnt >= length):
                    installing = False
                    cnt = 0
                if (j == N - 2) and installing:
                    can_install = False

            elif one_line[j] == one_line[j+1]+1:
                if installing:
                    can_install = False
                    break
                installing = True
                cnt = 1
                if N - j <= length:
                    can_install = False

            elif one_line[j]+1 == one_line[j+1]:
                if cnt >= length:
                    cnt = 1
                else:
                    can_install = False
                    break
            else:
                can_install = False
                break
        if can_install:
            install_number += 1

    #세로리스트 새로 생성
    row_list = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            row_list[i].append(board[j][i])

    for i in range(N):
        row_line = row_list[i]
        can_install = True
        installing = False
        row_cnt = 1
        for j in range(N - 1):
            if row_line[j] == row_line[j + 1]:
                row_cnt += 1
                if installing and row_cnt >= length:
                    installing = False
                    row_cnt = 0
                if j == N - 2 and installing:
                    can_install = False

            elif row_line[j] == row_line[j + 1] + 1:
                if installing:
                    can_install = False
                    break
                installing = True
                row_cnt = 1

                if j == N - 2 and installing:
                    can_install = False

            elif row_line[j] + 1 == row_line[j + 1]:
                if row_cnt >= length:
                    row_cnt = 1
                else:
                    can_install = False
                    break
            else:
                can_install = False
                break
        if can_install:
            install_number += 1

    print(f'#{tc} {install_number}')



