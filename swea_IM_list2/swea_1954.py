TC = int(input())
for tc in (1, TC+1):
    ri = [0,1,0,-1]
    ci = [1,0,-1,0]

    N = int(input())
    arr = [[0]*N for _ in range(N)]
    r, c, circle = 0, 0, 0
   

    for j in range(1, N**2 + 1):
        arr[r][c] = j
        r += ri[circle]
        c += ci[circle]

        if r < 0 or c < 0 or r >=N or c >= N or arr[r][c] != 0:
            r -= ri[circle]
            c -= ci[circle]
            circle = (circle + 1) % 4

            r += ri[circle]
            c += ci[circle]

    print(f'#{tc}')
    for u in arr:
        print(*u)
    


