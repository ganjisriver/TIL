N = int(input())
Fibo_list = [0 for _ in range(N+1)]

if N == 0 or N == 1:
    print(N)
    exit(0)
Fibo_list[1] = 1
for i in range(2, N+1):
    Fibo_list[i] = Fibo_list[i-1] + Fibo_list[i-2]
print(Fibo_list[N])