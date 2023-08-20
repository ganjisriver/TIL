import sys
input=sys.stdin.readline

N = int(input())
color_list = [[0,0,0]] + [list(map(int, input().split())) for _ in range(N)]
dp = [[0, 0, 0] for _ in range(N+1)]
dp[1] = color_list[1]
for i in range(2, N+1):
    for j in range(3):
        if j == 0:
            dp[i][j] = min(dp[i-1][1] + color_list[i][j], dp[i-1][2] + color_list[i][j])
        elif j == 1:
            dp[i][j] = min(dp[i-1][0] + color_list[i][j], dp[i-1][2] + color_list[i][j])
        else:
            dp[i][j] = min(dp[i-1][0] + color_list[i][j], dp[i-1][1] + color_list[i][j])

print(min(dp[-1]))