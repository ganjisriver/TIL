arr = []
for i in range(9):
    temp = list(map(int, input().split()))
    arr.append(temp)
max_value = 0
idx = (0, 0)
for i in range(9):
    for j in range(9):
        if max_value < arr[i][j]:
            max_value = arr[i][j]
            idx = (i, j)
print(max_value)
print(idx[0]+1, idx[1]+1)