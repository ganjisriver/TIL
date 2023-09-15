import heapq


def djikstra(start, end, limit_time):
    INF = 1e9
    result_list = [INF for _ in range(N+1)]
    result_list[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    while heap:
        min_value, idx = heapq.heappop(heap)
        if result_list[idx] < min_value:
            continue
        for node_idx in range(1, N+1):
            new_value = roads[idx][node_idx] + result_list[idx]
            if result_list[node_idx] > new_value:
                result_list[node_idx] = new_value
                heapq.heappush(heap, (new_value, node_idx))
        if idx == end:
            break

    if result_list[end] > limit_time:
        return False
    else:
        return True


N, M = map(int, input().split())
roads = [[0 for _ in range(N)]] + [[0] + list(map(int, input().split())) for _ in range(N)]

for i in range(M):
    start, end, limit_time = map(int, input().split())
    if djikstra(start, end, limit_time):
        print("Enjoy other party")
    else:
        print("Stay here")