T = input()
croa = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
three_croa = 'dz='
cnt = 0

for i in range(len(T)-1):
    for j in range(len(croa)):
        if T[i:i+2] == croa[j]:
            cnt += 1
for k in range(len(T)-2):
    if T[k:k+3] == three_croa:
        cnt += 1

answer = len(T) - cnt
print(answer)
