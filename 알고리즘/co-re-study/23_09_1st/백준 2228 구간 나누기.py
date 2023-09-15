N, M = map(int, input().split())
arr = [0] + [int(input()) for _ in range(N)]
dp = [[[0, 0] for _ in range(M+1)] for _ in range(N+1)]
dp[1][1][1] = arr[1]
for i in range(2, N+1):
    for j in range(M+1):
        if i < j:
            break
        if j == 0:
            dp[i][0][0] = dp[i-1][0][0]
        elif i == j:
            dp[i][j][1] = max(dp[i - 1][j][1] + arr[i], dp[i - 1][j - 1][0] + arr[i])
        else:
            dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1])
            dp[i][j][1] = max(dp[i-1][j][1] + arr[i], dp[i-1][j-1][0] + arr[i])
print(dp[-1][-1])