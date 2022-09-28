T = int(input())

for t in range(T):
    N = (int(input())) // 10
    count = 1

    for i in range(1, N + 1):
        n = (i // 2)
        if n != 0:
            count += 2 ** (n*2 - 1)

    print(f'#{t + 1} {count}')