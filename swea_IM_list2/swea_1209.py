for TC in range(1, 11):
    tc = int(input())

    
    
        arr = [list(map(int, input().split())) for _ in range(100)]
        
    row_max = 0
    
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += arr[i][j]
        
        if sum > row_max:
            row_max = sum

    col_max = 0
    for i in range(100):
        sum = 0
        for j in range(100):
            sum+=arr[j][i]
        if sum > col_max:
            col_max = sum

    for i in range(100):
        sum = 0
        sum += arr[i][i]
    
    left_dia = sum
    
    for i in range(100):
        sum = 0
        sum += arr[i][99-i]
    
    right_dia = sum

    max_value = max(row_max, col_max, left_dia, right_dia)
    print(f'#{TC} {max_value}')
        
