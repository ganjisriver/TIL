memo = [1, 1, 3]
def jong(n):
    global memo
    s = int(n/10)
    if len(memo) <= s:
        memo.append(jong(n-10) + (jong(n-20)*2))

    return memo[int(n/10)]

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    print(f'#{tc} {jong(N)}')