max_value = 0
max_idx = 0
N_list = []
for i in range(9):
    N = int(input())
    N_list.append(N)
for idx, value in enumerate(N_list, start=1):
    if max_value < value:
        max_value = value
        max_idx = idx

print(max_value)
print(max_idx)