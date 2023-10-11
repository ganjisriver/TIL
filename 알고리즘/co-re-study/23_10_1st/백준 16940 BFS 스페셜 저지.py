from collections import deque
import sys
input=sys.stdin.readline

def BFS(order):
    q = deque([1])
    visited = [0 for _ in range(N+1)]
    visited[1] = 1
    idx = 1
    while q:
        current = q.popleft()
        adj_nodes = set()
        for dest in adj_list[current]:
            if not visited[dest]:
                visited[dest] = 1
                adj_nodes.add(dest)
        for _ in range(len(adj_nodes)):
            if order[idx] in adj_nodes:
                q.append(order[idx])
            else:
                print(0)
                exit(0)
            idx += 1

    print(1)


N = int(input())
adj_list = [[] for _ in range(N+1)]
for i in range(1, N):
    x, y = map(int, input().split())
    adj_list[x].append(y)
    adj_list[y].append(x)

answer_candi = list(map(int, input().split()))
BFS(answer_candi)



