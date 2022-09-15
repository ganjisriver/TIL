def sum_idx(idx):
    global result
    if idx == 0:
        return
    else:
        result += tree_idx[idx//2]
        sum_idx(idx//2)

def swap(i):
    if i > N:
        return
    if tree_idx[i//2] and (tree_idx[i] < tree_idx[i // 2]):
        tree_idx[i], tree_idx[i // 2] = tree_idx[i // 2], tree_idx[i]
        swap(i//2)



TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    tree_idx = [0]+list(map(int, input().split()))
    result = 0
    for i in range(1, N+1):
        swap(i)
    sum_idx(N)
    print(f'#{tc} {result}')





