V, E = map(int, input().split())

matrix = [[0]*(V+1) for _ in range(V+1)]

node = list(map(int, input().split()))
for i in range(len(node)//2):
    start = node[i*2]
    end = node[i*2+1]
    matrix[start][end] = 1
    matrix[end][start] = 1

q = [1]
visited = []

while q:
    current = q.pop(0)
    if current not in visited:
        visited.append(current)

    for destination in range(V+1):
        if matrix[current][destination] and destination not in visited:
            q.append(destination)

print(*visited)