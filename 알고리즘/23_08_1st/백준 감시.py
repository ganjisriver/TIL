from collections import deque
CCTV_dict = {1: [[(0, 1)], [(-1, 0)], [(1, 0)], [(0, -1)]],
             2: [[(0, -1), (0, 1)], [(-1, 0), (1, 0)]],
             3: [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)]],
             4: [[(0, -1), (-1, 0), (0, 1)], [(0, -1), (-1, 0), (1, 0)], [(0, -1), (0, 1), (1, 0)], [(0, 1), (-1, 0), (1, 0)]],
             5: [(-1, 0), (1, 0), (0, -1), (0, 1)]}

N, M = map(int, input().split())
office_map = [list(map(int, input().split())) for _ in range(N)]
CCTV_index = deque()
walls = []
for i in range(N):
    for j in range(M):
        if office_map[i][j]:
            if office_map[i][j] == 6:
                walls.append((i, j))
            else:
                CCTV_index.append((i, j))

visited = set()

while CCTV_index:
    CCTV_index.popleft()

