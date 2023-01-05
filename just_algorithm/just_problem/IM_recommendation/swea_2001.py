TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_value = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            cnt = 0
            for k in range(M):
                for u in range(M):
                    cnt += matrix[i+k][j+u]
            if max_value < cnt:
                max_value = cnt
    print(f'#{tc} {max_value}')
