# 크루스칼 최소값구하기
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

# 프림 방법
# def Prim():
#     dist = [987654321] * (V+1)
#     dist[V] = 0
#     visited = [False] * (V+1)
#
#     for _ in range(V+1):
#         min_idx = -1
#         min_value = 987654321
#
#         for i in range(V+1):  # 일단 현재 dist 배열에서 visited 안된애들 중 가장 노드 찾는 로직
#             if not visited[i] and dist[i] < min_value:
#                 min_idx = i
#                 min_value = dist[i]  # 갱신!
#
#         visited[min_idx] = True  # 가장 작은애로 이동할거니까 visited 넣어주고
#         # 요거 주석 풀어서 visted, dist 찍어볼것!
#         print(visited, dist)
#
#         # 이제 그 선택된 점에서부터 갈 수 있되, 더 짧은 거리를 보장한다면 dist 배열 갱신
#         for i in range(V+1):
#             if not visited[i] and adj[min_idx][i] < dist[i]:
#                 dist[i] = adj[min_idx][i]
#
#     return sum(dist)  # 마지막에 dist 배열의 총합산이 MST를 이루는 간선들의 합
#
#
# for tc in range(1, int(input())+1):
#     V, E = map(int,input().split())
#
#     adj = [[987654321] * (V+1) for _ in range(V+1)]  # inf 개념으로 큰 수 넣어줌
#
#     for i in range(E):  # 인접행렬 만들기
#         st, ed, w = map(int, input().split())
#         adj[st][ed] = adj[ed][st] = w  # 노드들간의 가중치 자체를 인접 행렬에 넣어서 구조화
#
#     print("#{} {}".format(tc, Prim()))

# 다익스트라
def dijkstra():
    dist = [987654321] * (V+1)
    dist[0] = 0  # 여기 start 점을 넣어주면 됨.
    visited = [False] * (V+1)

    for _ in range(V+1):
        min_idx = -1
        min_value = 987654321

        for i in range(V+1):  # 일단 현재 dist 배열에서 visited 안된애들 중 가장 노드 찾는 로직
            if not visited[i] and dist[i] < min_value:
                min_idx = i
                min_value = dist[i]  # 갱신!

        visited[min_idx] = True  # 가장 작은애로 이동할거니까 visited 넣어주고
        # 요거 주석 풀어서 visted, dist 찍어볼것!
        # print(visited, dist)

        # 이제 그 선택된 점에서부터 갈 수 있되, 더 짧은 거리를 보장한다면 dist 배열 갱신
        for i in range(V+1):
            if not visited[i] and adj[min_idx][i] < dist[i]:
                dist[i] = adj[min_idx][i]
    return sum(dist)


for tc in range(1, int(input())+1):
    V, E = map(int,input().split())

    adj = [[987654321] * (V+1) for _ in range(V+1)]  # inf 개념으로 큰 수 넣어줌

    for i in range(E):  # 인접행렬 만들기
        st, ed, w = map(int, input().split())
        adj[st][ed] = adj[ed][st] = w  # 노드들간의 가중치 자체를 인접 행렬에 넣어서 구조화

    print("#{} {}".format(tc, dijkstra()))

