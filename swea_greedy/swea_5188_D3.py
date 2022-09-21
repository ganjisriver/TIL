dr = [1, 0]
dc = [0, 1]

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_value = 0
    r, c = 0
    i = 0
    total = arr[0][0]
    while True:
        if min_value > total:
            min_value = total

        for i in range(2):
            r = r+dr[i]
            c = c+dc[i]

        if 0 <= r <= N-1 and 0 <= c <= N-1:
