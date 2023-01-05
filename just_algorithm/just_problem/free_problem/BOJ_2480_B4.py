noon_list = list(map(int, input().split()))
matrix = [0]*7

for i in range(3):
    matrix[noon_list[i]] += 1
result = 0
max_result = 0
for i in range(1, 7):
    if matrix[i] == 3:
        result  = 10000+(i*1000)

    if matrix[i] == 2:
        result = 1000+(i*100)

    if max_result <= matrix[i]:
        max_result = matrix[i]
        idx = i
        if max_result == 1:
            result = idx*100

print(result)
