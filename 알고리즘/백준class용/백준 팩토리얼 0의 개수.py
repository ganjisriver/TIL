N = int(input())
N_factorial = 1
answer = 0
for i in range(N):
    N_factorial = N_factorial*(N-i)
N_factorial_toString = str(N_factorial)
for i in range(len(N_factorial_toString)-1, 0, -1):
    if N_factorial_toString[i] == '0':
        answer += 1
    else:
        break


print(answer)