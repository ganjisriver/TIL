

TC = int(input())
for tc in range(1, TC+1):
    N, M, L = map(int, input().split())
    tree_idx = [0]*(N+1)
    for _ in range(M):
        node_number, node_result = map(int, input().split())
        tree_idx[node_number] = node_result

    for i in range(N):
        if N % 2 == 1:
            if tree_idx[i] and tree_idx[i//2] == tree_idx[(i+1)//2]:
                tree_idx[i//2] = tree_idx[i] + tree_idx[i+1]
        else:

    print(tree_idx)