A, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(B)]

for i in range(A-7):
    for j in range(B-7):
        for k in range(i, i+8):
            for u in range(i, i+8):
                if arr[i+k][j+u]: