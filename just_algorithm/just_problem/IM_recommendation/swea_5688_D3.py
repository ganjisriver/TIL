TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    result = -1
    for i in range(1, 1000001):
        if i**3 == N:
            result = i
            break
    print(f'#{tc} {result}')