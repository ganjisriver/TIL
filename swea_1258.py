# swea 1258번  7일차 행렬찾기

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    minimum = 0
    maximum = 0
    row = maximum - minimum
    S =[]
    for i in range(N):
        for j in range(N-1):
            while True:
                k = 0
                if matrix[i+k][j] != 0 and matrix[i+k][j+1] == 0:
                    minimum = i
                else:
                    maximum = i+k
                    break
                k += 1
    # for i in range(N):
    #     for j in range(N):
    #         if S[i][1] == S[i+1][1]:

    print(S)