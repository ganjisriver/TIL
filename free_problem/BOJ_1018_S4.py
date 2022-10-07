N, M = map(int, input().split())
board = [input() for _ in range(N)]
for i in range(N-7):
    for j in range(M-7):

        for r in range(8):
            for c in range(8):