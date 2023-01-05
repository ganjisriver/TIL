TC = int(input())
for tc in range(1, TC+1):
    matrix = [list(map(int, input().split())) for _ in range(9)]
    flag = True
    for i in range(9):
        idx = [0] * 10
        for j in range(9):
            idx[matrix[i][j]] += 1
            if idx[matrix[i][j]] > 1:
                flag = False
                break
        if not flag:
            print(f'#{tc} 0')
            break
    if flag:
        for i in range(9):
            idx = [0] * 10
            for j in range(9):
                idx[matrix[j][i]] += 1
                if idx[matrix[i][j]] > 1:
                    flag = False
                    print(f'#{tc} 0')
                    break
            if not flag:
                break

    if flag:
        for i in range(3):
            for j in range(3):
                idx = [0] * 10
                for k in range(3):
                    for u in range(3):
                        idx[matrix[i*3+k][j*3+u]] += 1
                        if idx[matrix[i*3+k][j*3+u]] > 1:
                            flag = False
                            print(f'#{tc} 0')
                            break
                    if not flag:
                        break
                if not flag:
                    break
            if not flag:
                break
    if flag:
        print(f'#{tc} 1')

