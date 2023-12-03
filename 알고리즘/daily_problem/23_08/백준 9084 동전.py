T = int(input())
for tc in range(T):
    N = int(input())
    coin_kind_list = list(map(int, input().split()))
    target = int(input())
    dp = [0 for _ in range(target+1)]
    dp[0] = 1
    for coin in coin_kind_list:
        for i in range(target+1):
            if i >= coin:
                dp[i] += dp[i-coin]
    print(dp[target])