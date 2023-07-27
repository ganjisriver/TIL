def find_root(x):
    if x != root[x]:
        return find_root(root[x])
    else:
        return x


def union(x, y):
    if root[x] == root[y]:
        return
    else:
        x = find_root(x)
        y = find_root(y)
        if rank[x] > rank[y]:
            rank[y] = rank[x]
            root[y] = root[x]
        elif rank[x] == rank[y]:
            rank[x] += 1
            root[y] = x
        else:
            rank[x] = rank[y]
            root[x] = root[y]


N, M, K = map(int, input().split())
candis_num = [0]+list(map(int, input().split()))
root = [i for i in range(N+1)]
rank = [1]*(N+1)
zip_dan = dict()

for i in range(M):
    friend1, friend2 = map(int, input().split())
    if find_root(friend1) != find_root(friend2):
        union(friend1, friend2)

#
visited = set()
for i in range(1, len(root)):
    if root[i] not in visited:
        zip_dan[root[i]] = (candis_num[i], 1)
        visited.add(root[i])
    else:
        zip_dan[root[i]] = (zip_dan[root[i]][0] + candis_num[i], zip_dan[root[i]][1] + 1)
zip_dan_list = []
for i in visited:
    zip_dan_list.append(zip_dan[root[i]])
zip_dan_list.sort(key=lambda x: (-x[0], x[1]))
dp = []

print(f"candis_num: {zip_dan_list}")
print(f"root: {root}")
print(f"rank: {rank}")
