N, K = map(int, input().split())
jewly_list = [[0,0]]
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
for i in range(N):
    weight, value = map(int, input().split())
    jewly_list.append([weight, value])

for i in range(N+1):
    for j in range(K+1):
        weight = jewly_list[i][0]
        value = jewly_list[i][1]

        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-weight] + value, dp[i-1][j])
print(dp[N][K])


