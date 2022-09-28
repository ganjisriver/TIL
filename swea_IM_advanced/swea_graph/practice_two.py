matrix = [[0]*10 for _ in range(10)]

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

    for destination in range(10):
        if matrix[current][destination] and destination not in visited:
            q.append(destination)

print(*visited)