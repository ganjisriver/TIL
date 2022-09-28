def container(x):
    global b, total
    if b >= x:
        total += x
        return total
    if not N_list:
        return total

    if b < x:
        c = N_list.pop(0)
        container(c)



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))
    M_list = list(map(int, input().split()))
    N_list.sort(reverse=True)
    M_list.sort(reverse=True)
    total = 0
    while N_list and M_list:
        a = N_list.pop(0)
        b = M_list.pop(0)
        if b >= a:
            total += a
        elif b < a:
            container(a)

    print(f'#{tc} {total}')