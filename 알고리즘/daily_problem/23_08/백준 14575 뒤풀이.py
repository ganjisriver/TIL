N, T = map(int, input().split())
max_Li = 0
max_Ri = 0
alchol_list = []
for i in range(N):
    Li, Ri = map(int, input().split())
    if max_Li < Li:
        max_Li = Li
    if max_Ri < Ri:
        max_Ri = Ri
    alchol_list.append((Li, Ri))
start, end = max_Li, max_Ri

R = -1
while start < end:
    mid = (start + end) // 2
    min_T = 0
    max_R = mid*N
    for Li, Ri in alchol_list:
        min_T += Ri
        if mid < Ri:
            end = mid-1

    if min_T <= T < max_R:
        start = mid + 1

print(max_Ri)



