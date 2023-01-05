N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        