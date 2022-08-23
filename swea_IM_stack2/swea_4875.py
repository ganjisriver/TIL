TC = int(input())
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]
for tc in range(1, TC+1):
    N = int(input())
    matrix = [list(map(int, list(input()))) for _ in range(N)]

    initial_r = None
    initial_c = None
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                initial_r = i
                initial_c = j
                break
    stack = []
    visited = set()
    visited.add((initial_r, initial_c))
    r, c = (initial_r, initial_c)

    for i in range(4):

        if r < 0 and r >= N or c < 0 and c >= N:
            continue

        if  or (r,c) in visited:

