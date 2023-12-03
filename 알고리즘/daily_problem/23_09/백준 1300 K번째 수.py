N = int(input())
K = int(input())
start = 1
end = min(10**9, N*N)
while start <= end:
    mid = (start + end) // 2
    K_candi = 0
    for i in range(1, N+1):
        K_candi += min(mid//i, N)
        if K_candi > K:
            break

    if K_candi >= K:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer)
