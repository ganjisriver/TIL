d, N, M = map(int, input().split())

stones = [int(input()) for _ in range(N)] + [d]
stones.sort()
start, end = 0, d
dist = 0
while start <= end:
    mid = (start + end) // 2
    now = 0
    break_cnt = 0
    for stone in stones:
        if stone - now >= mid:
            now = stone
        else:
            break_cnt += 1
    if break_cnt <= M:
        start = mid + 1
        dist = mid
    else:
        end = mid - 1
print(dist)
