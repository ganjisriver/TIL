def combinations(N):
    for i in range(1, N+1):
        for j in range(i+1, N):
            for k in range(j+1, N-1):

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    C_list = []
    for
    print(C_list)


    # for i in range(N):
    #     for j in range(N):
    #         if i < j :
    #             c = arr[j][i] + arr[i][j]
    #             C_list.append(c)
    #
    # print(C_list)
    # for i in range(len(C_list)):
