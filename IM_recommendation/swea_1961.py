TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    new_matrix = [[0] * 3 for _ in range(N)]

    for i in range(N):
        temp = []
        for j in range(N):
            temp.append(matrix[j][i])
        temp.reverse()
        new_matrix[i][0] = (''.join(map(str, temp)))

    for i in range(N):
        temp = []
        for j in range(N):
            temp.append(matrix[N - 1 - i][N - 1 - j])
        new_matrix[i][1] = (''.join(map(str, temp)))
    temp_matrix = []

    for i in range(N):
        temp = []
        for j in range(N):
            temp.append(matrix[j][i])
        temp_matrix.append(temp)
    temp_matrix.reverse()

    for i in range(N):
        new_matrix[i][2] = ''.join(map(str, temp_matrix[i]))

    print(f'#{tc}')
    for i in range(N):
        a = ' '.join(new_matrix[i])
        print(a)



