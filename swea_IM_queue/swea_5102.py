# TC = int(input())
# for tc in range(1, TC+1):
#     V, E = map(int, input().split())
#     matrix = [[0]*(V+1) for _ in range(V+1)]
#
#     for _ in range(E):
#         start, end = map(int, input().split())
#         matrix[start][end] = 1
#         matrix[end][start] = 1
#     S, G = map(int, input().split())
#     stack = [1]
#     visited = []
#     cool = 0
#     flag = True
#     while flag:
#         cnt = 0
#         current = stack.pop()
#         if current not in visited:
#             visited.append(current)
#
#         for destination in range(V+1):
#             if matrix[current][destination] and destination not in visited and destination not in stack:
#                 stack.append(destination)
#             if matrix[current][destination] and destination not in visited:
#                 cnt += 1
#         if cnt == 0:
#             for destination in range(V+1):
#                 if matrix[current][destination] and destination not in stack:
#                     stack.append(destination)
#                     visited.append(destination)
#                     break
#         for i in range(len(visited)):
#             if visited[i] == 1:
#                 cool += 1
#                 if cool == 5:
#                     break
#         if cool == 5:
#             break
#     min_value = 1000000
#     for i in range(len(visited)):
#         if visited[i] == S:
#             S = i
#         if visited[i] == G:
#             G = i
#         if min_value > G-S > 0 :
#             min_value = G-S
#
#     print(f'#{tc} {min_value}')

TC = int(input())
for tc in range(1, TC+1):
    V, E = map(int, input().split())            # V = 노드의 개수, E = 간선의 개수
    matrix = [[0]*(V+1) for _ in range(V+1)]    # 인접행렬로 풀기 위한 matrix 생성
    for _ in range(E):                          # 간선을 이어주는 작업
        start, end = map(int, input().split())
        matrix[start][end] = 1
        matrix[end][start] = 1
    S, G = map(int, input().split())            # S = 시작지점, G = 목표 지점

    result = 0                                  # 이후의 결과값 넣어주기 위한 변수 지정
    q = [S]                        # queue 생성
    visited = [0]*(V+1)                         # visited를 인덱스로 넣어주기 위한 작업
    distance = [0]*(V+1)                        # 노드(idx)별 거리를 넣기 위한 distance 생성
    while q:
        current = q.pop(0)
        for destination in range(V+1):
            if matrix[current][destination] and not visited[destination]:   # 간선이 있고, 목적지에 visited 넣어주기
                q.append(destination)                                       # queue에 목적지 넣어주기
                visited[destination] = 1                                    # 목적지 인덱스에 1넣고 방문했다고 표시
                distance[destination] = distance[current] + 1               # 현재 거리보다 +1 해줌으로써, 최종적으로 목표지점에 도달했을 때 거리를 계산할 예정
                if destination == G:                                        # 목표 지점에 도달 했을 때,
                    result = distance[destination]                          # result에 그 거리 지정
    print(f'#{tc} {result}')

