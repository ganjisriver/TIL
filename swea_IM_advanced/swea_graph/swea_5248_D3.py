def make_set(x):
    p[x] = x


def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    p[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    students = list(map(int, input().split()))
    p = [0]*(N+1)
    groups = set()
    for i in range(N+1):
        make_set(i)
    for i in range(M):
        x, y = students[2*i], students[2*i+1]
        if find_set(x) != find_set(y):
            union(x, y)

    for i in range(1, N+1):
        groups.add(find_set(i))

    print(f'#{tc} {len(groups)}')
