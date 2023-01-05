N = int(input())
N_list = []
for i in range(N):
    s = int(input())
    N_list.append(s)
N_list.sort()
for i in range(N):
    print(N_list[i])