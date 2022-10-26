N = int(input())
idx_list = []
for i in range(N):
    (x, y) = tuple(map(int, input().split()))
    idx_list.append((x, y))

idx_list.sort()
for i in range(N):
    (x, y) = idx_list[i]
    print(x, y)