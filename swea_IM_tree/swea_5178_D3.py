TC = int(input())
for tc in range(1, TC+1):
    N, M, L = map(int, input().split())
    tree_idx = [0]*(N+1)
    for _ in range(M):
        node_number, node_result = map(int, input().split())
        tree_idx[node_number] = node_result


        if N % 2 == 0:
            tree_idx.append(0)
        for i in range(N, 1, -2):
            tree_idx[i // 2] = tree_idx[i//2*2] + tree_idx[i//2*2 + 1]
    print(f'#{tc} {tree_idx[L]}')