def inorder(N):
    global cnt
    if N:
        cnt += 1
        inorder(left[N])
        inorder(right[N])

TC = int(input())
for tc in range(1, TC+1):
    E, N = map(int, input().split())
    tree_idx = list(map(int, input().split()))
    left = [0]*(E+2)
    right = [0]*(E+2)

    for i in range(E):
        p, c = tree_idx[2*i], tree_idx[(2*i)+1]
        if left[p]:
            right[p] = c
        else:
            left[p] = c
    cnt = 0
    inorder(N)
    print(f'#{tc} {cnt}')
