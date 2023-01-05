TC = int(input())
for tc in (1, TC+1):
    K, N, M = map(int, input().split())
    cell_stop = list(map(int, input().split()))

    bus_stop = [0]*(N+1)
    cnt = 0
    for i in cell_stop:
        bus_stop[i] += 1
    bus_position = 0
    while bus_position < N-K:
        arriving = 0
        for j in range(K, 0, -1):
            if bus_stop[bus_position+j] == 0:
                continue
            else:
                bus_position += j
                arriving = 1
                cnt += 1
                break
        if arriving == 0 or bus_position + K == N:
            break
    if arriving == 0:
        print(f'#{tc} 0')
    
    else:
        print(f'#{tc} {cnt}')
    
    
    
    
    