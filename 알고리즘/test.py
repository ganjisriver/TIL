# Union-find 알고리즘 구현
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n, m = 3, 3
parent = [i for i in range(n+1)]

# 적대적인 관계를 Union-find 알고리즘으로 묶어 줌
for _ in range(m):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 적의 적은 나의 친구인지 검증
for i in range(1, n+1):
    for j in range(i+1, n+1):
        if find_parent(parent, i) != find_parent(parent, j):
            # 두 노드가 서로 다른 집합에 속하면 공통적인 적을 찾아 같은 집합으로 묶어 줌
            for k in range(1, n+1):
                if find_parent(parent, i) == find_parent(parent, k) and find_parent(parent, j) == find_parent(parent, k):
                    union_parent(parent, i, j)
                    break

# 결과 출력
if find_parent(parent, 1) == find_parent(parent, 2) and find_parent(parent, 1) == find_parent(parent, 3):
    print("적의 적은 나의 친구입니다.")
else:
    print("적의 적은 나의 친구가 아닙니다.")