a = int(input())

for i in range(a):
    b = list(map(int, input().split()))
    
    print(f'#{i+1} {max(b)}')
        