from itertools import combinations
flower = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]


def flowering(candidate_tuple):
    global min_cost
    cost = 0
    visited = []
    for r, c in candidate_tuple:
        for k in range(5):
            nr = r + flower[k][0]
            nc = c + flower[k][1]
            if (nr, nc) in visited:
                return
            else:
                visited.append((nr, nc))
                cost += cost_arr[nr][nc]
    if cost < min_cost:
        min_cost = cost


N = int(input())
cost_arr = [list(map(int, input().split())) for _ in range(N)]
flower_arr = [(r, c) for r in range(1, N-1) for c in range(1, N-1)]
min_cost = 999999999
flower_combi = list(combinations(flower_arr, 3))

for flower_candidate in flower_combi:
    flowering(flower_candidate)

print(min_cost)


