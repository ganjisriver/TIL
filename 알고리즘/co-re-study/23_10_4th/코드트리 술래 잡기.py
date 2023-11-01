n, m, h, k = map(int, input().split())
arr = [[[] for _ in range(n)] for _ in range(n)]
domang_idx_list = []
sulae_idx = [n//2, n//2, 0]
for i in range(m):
    x, y, move_type = map(int, input().split())
    arr[x][y].append(move_type)
    domang_idx_list.append([x, y, move_type])

for i in range(h):
    x, y = map(int, input().split())
    arr[x][y].append(3)

sulae_idx = [n//2, n//2]
arr[sulae_idx[0]][sulae_idx[1]] = 9