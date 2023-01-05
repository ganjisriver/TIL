def perm(depth, acc):
    global min_value

    if acc > min_value:
        return

    if depth == n:
        if min_value > acc:
            min_value = acc

        return
    mat = arr[depth]
    for i in range(n):
        if not check[i]:
            acc += mat[i]
            check[i] = 1
            perm(depth+1, acc)
            check[i] = 0
            acc -= mat[i]

TC = int(input())
for tc in range(1, TC+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    sel = [0] * n
    check = [0] * n
    min_value = 9999999999
    perm(0, 0)
    print(f'#{tc} {min_value}')