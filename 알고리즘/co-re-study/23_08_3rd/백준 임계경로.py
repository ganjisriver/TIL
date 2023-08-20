N = int(input())
M = int(input())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
degree = [0 for _ in range(N+1)]
graph_dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(M):
    start, end, time = map(int, input().split())
    graph[start][end] = time
    graph[end][start] = time
    degree[start] += 1
    degree[end] += 1
start_city, end_city = map(int, input().split())




