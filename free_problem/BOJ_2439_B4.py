N = int(input())
for i in range(1, N+1):
    a = ' '*(N-i)
    b = '*'*i
    print(f'{a}{b}')
