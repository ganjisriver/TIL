dr = [1, 1, -1, -1]
dc = [1, -1, 1, -1]

def finding(depth, idx):
    queen = arr[depth][idx]
    arr[depth][:] = 1   # 가로 1적용

    for i in range(N):  # 세로 1 적용
        arr[i][idx] = 1
    for i in range(N):
        for j in range(4):
        arr[depth+dr][idx+dc]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    cnt = 0
