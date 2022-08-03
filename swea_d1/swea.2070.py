a = int(input())

for i in range(1, a+1):
    b = list(map(int, input().split()))
    if b[0] > b[1]:
        print(f'#{i} >')
    elif b[0] == b[1]:
        print(f'#{i} =')
    
    elif b[0] < b[1]:
        print(f'#{i} <')
    
    