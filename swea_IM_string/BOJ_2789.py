T = list(input())
r_list = ['C', 'A', 'M', 'B', 'R', 'I', 'G', 'E']
for i in range(len(T)):
    if r_list[i] in T:
        T.remove(r_list[i])
N =''.join(T)
print(N)
