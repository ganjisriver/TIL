A = int(input())
B = int(input())
C = int(input())
idx_list = [0]*10
result = str(A*B*C)
for i in result:
    idx_list[int(i)] += 1

for i in range(len(idx_list)):
    print(idx_list[i])
