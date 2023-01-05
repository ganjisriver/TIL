TC = int(input())
for tc in range(1, TC+1):
    length = int(input())
    
    arr = [list(map(int, input().split())) for _ in range(length)]

    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    total_sum = 0
    for i in range(length):
        for j in range(length):
            absolute_sum = 0
            for direction in range(4):
                r = i + dr[direction]
                c = j + dc[direction]   

                if 0<= r <= length-1 and 0 <= c <= length-1:
                    absolute_sum = arr[i][j] - arr[r][c]
                    if absolute_sum < 0:
                        absolute_sum = -(absolute_sum)
                        total_sum += absolute_sum
                    else: 
                        absoulte_sum = absolute_sum
                        total_sum += absolute_sum

                        
                    
    
    print(f'#{tc} {total_sum}')
            
            