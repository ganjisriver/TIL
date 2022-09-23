T = list(input())
r_list = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']
case = []
for i in range(len(T)):
    if T[i] in r_list:
        T[i] = 0
for i in range(len(T)):
    if T[i] != 0:
        case.append(T[i])

answer = ''.join(case)
print(answer)