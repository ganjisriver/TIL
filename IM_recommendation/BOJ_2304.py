N = int(input())
min_value = 1001
max_value = 0
N_list = []
result = 0
for i in range(N):
    (idx, height) = map(int, input().split())
    N_list.append((idx, height))
    if min_value > idx:
        min_value = idx
    if max_value < idx:
        max_value = idx
idx_list = [0]*(max_value+1)

for i in range(len(N_list)):
    idx_list[N_list[i][0]] = N_list[i][1]

for i in range(len(idx_list)):
    for j in range(len(idx_list)-i):
        if idx_list[i] < idx_list[i+j]:
            result += j*idx_list[i]
        elif idx_list[i] > idx_list[i+j]:
