# dp를 써야하는 이유 이해 안됨

N = int(input())

if N <= 3:
    print(0)
    exit()

if N == 4:
    print(13)
    exit()
cnt = 13
K = 48
T = 1
while K > 52 - N:
    cnt = cnt*K/T
    K -= 1
    T += 1
print(int(cnt % 10007))