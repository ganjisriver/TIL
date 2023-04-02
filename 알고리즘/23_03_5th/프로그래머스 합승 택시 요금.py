# import heapq
#
#
# def dijkstra(graph, start):
#     INF = 99999999999999999
#     distances = {node:INF  for node in graph}
#     distances[start] = 0
#
#     visited = set()
#
#     heap = [(0, start)]
#
#     while heap:
#         (current_distance, current_node) = heapq.heappop(heap)
#
#         if current_node in visited:
#             continue
#
#         for neighbor, weight in graph[current_node].items():
#             distance = current_distance + weight
#             if distance < distances[neighbor]:
#                 distances[neighbor] = distance
#                 heapq.heappush(heap, (distance, neighbor))
#
#         visited.add(current_node)
#
#     return distances
#
# graph = {
#     1: {2: 3, 3: 2, 4: 7},
#     2: {5: 1},
#     3: {4: 1, 6: 4},
#     4: {6: 2},
#     5: {6: 3},
#     6: {}
# }
#
# distances = dijkstra(graph, 1)
# print(distances)

INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

def floyd_warshall(n, edges):
    # 초기 그래프 생성
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        graph[i][i] = 0  # 자기 자신과의 거리는 0

    # 간선 정보 입력
    for a, b, cost in edges:
        graph[a][b] = cost
        graph[b][a] = cost  # 양방향 그래프이므로 반대도 추가

    # 플로이드-워셜 알고리즘 수행
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    return graph

# 예시 입력
n = 6  # 노드 개수
edges = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

# 플로이드-워셜 알고리즘 수행 및 출력
result = floyd_warshall(n, edges)
for row in result[1:]:  # 0번 노드는 사용하지 않으므로 제외
    print(row[1:])