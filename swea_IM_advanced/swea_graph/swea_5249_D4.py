# def make_set(x):
#     p[x] = x
#
#
# def find_set(x):
#     if p[x] != x:
#         p[x] = find_set(p[x])
#     return p[x]
#
#
# def union(x, y):
#     p[find_set(y)] = find_set(x)
#
#
# T = int(input())
# for tc in range(1, T+1):
#     V, E = map(int, input().split())
#     matrix = [list(map(int, input().split())) for _ in range(E)]
#     matrix.sort(key=lambda x: x[2])
#     p = [0]*(V+1)
#     for i in range(V+1):
#         make_set(i)
#     cnt = 0
#     answer = 0
#     for x, y, m in matrix:
#         if find_set(x) != find_set(y):
#             union(x, y)
#             answer += m
#             cnt += 1
#         if cnt == V:
#             break
#     print(f'#{tc} {answer}')
# def prim():
#     d
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    matrix = [[987654321]*(V+1) for _ in range(V+1)]
    for i in range(E):
        s, e, w = map(int, input().split())
        matrix[s][e] = matrix[e][s] = w

