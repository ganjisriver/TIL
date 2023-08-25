from collections import deque
import sys
input = sys.stdin.readline
direction = [(1, 0), (0, 1)]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
visited[0][0] = 1
start = (0, 0)
q = deque([start])

while q:
    x, y = q.pop()
    for i in range(2):
        dx, dy = x + direction[i][0]*arr[x][y], y + direction[i][1]*arr[x][y]
        if (dx, dy) == (N-1, N-1):
            print("HaruHaru")
            exit(0)
        if 0 <= dx < N and 0 <= dy < N:
            if not visited[dx][dy]:
                q.append((dx, dy))
                visited[dx][dy] = 1
print("Hing")

