idx = [0]*31
for i in range(28):
    N = int(input())
    idx[N] = 1

for i in range(1, 31):
    if not idx[i]:
        print(i)