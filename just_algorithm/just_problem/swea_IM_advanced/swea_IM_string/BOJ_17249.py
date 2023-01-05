A = list(map(str, input()))

left_cnt = 0
right_cnt = 0
for i in range(len(A)):
    if A[i] == '@':
        left_cnt += 1
    else:
        if A[i] == '(':
            j = i
            break

for k in range(j+4, len(A)):
    if A[k] == '@':
        right_cnt += 1
print(f'{left_cnt} {right_cnt}')

