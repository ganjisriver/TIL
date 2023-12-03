T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    M_factorial = 1
    for i in range(1, M+1):
        M_factorial = M_factorial*i
    N_factorial = 1
    for i in range(1, N+1):
        N_factorial = N_factorial*i
    M_N_factorial = 1
    for i in range(1, M-N+1):
        M_N_factorial = M_N_factorial*i
    answer = M_factorial // (N_factorial * M_N_factorial)
    print(answer)