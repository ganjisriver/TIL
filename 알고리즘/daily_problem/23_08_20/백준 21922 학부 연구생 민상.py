'''
진짜 필요 없는 거 최대한 덜어내고 덜어내야 풀림..
bfs로 하면 안되고, dfs로 하니 풀림..
'''


from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상 하 좌 우
change_direction_dict = {0: [0, 1, 2, 3],
                         1: [0, 1, 3, 2],
                         2: [1, 0, 2, 3],
                         3: [3, 2, 1, 0],
                         4: [2, 3, 0, 1]}
reverse_direction_dict = {0: [0, 1, 2, 3],
                          1: [1, 0, 2, 3],
                          2: [0, 1, 3, 2],
                          3: [2, 3, 0, 1],
                          4: [3, 2, 1, 0]}


arr = []
visited = [[[0, 0, 0, 0] for _ in range(M)] for _ in range(N)]
dfs_stack = deque([])
answer_visited = set()
for i in range(N):
    arr_list = list(map(int, input().split()))
    for j in range(M):
        if arr_list[j] == 9:
            answer_visited.add((i, j))
            dfs_stack.append((i, j, [0, 1, 2, 3]))
    arr.append(arr_list)

while dfs_stack:
    current = dfs_stack.pop()
    for i in range(len(current[2])):
        current_direction = current[2][i]
        dr = current[0] + direction[current_direction][0]
        dc = current[1] + direction[current_direction][1]
        if 0 <= dr < N and 0 <= dc < M:
            if visited[dr][dc][current_direction] or arr[dr][dc] == 9:
                continue
            new_direction = change_direction_dict[arr[dr][dc]][current_direction]
            reverse_direction = reverse_direction_dict[arr[dr][dc]][current_direction]
            if arr[dr][dc] == 1 or arr[dr][dc] == 2:
                if current[2][i] == reverse_direction:
                    answer_visited.add((dr, dc))
                    continue
            visited[dr][dc][current_direction] = 1
            visited[dr][dc][reverse_direction] = 1
            answer_visited.add((dr, dc))
            dfs_stack.append((dr, dc, [new_direction]))
print(len(answer_visited))

'''
visited를 3차원으로 하는 대신, set()을 넣어봤는데, 메모리초과가 떠서, 확실히 set()은 조금 부담 되는 것 같음.
'''
# dr, dc 방향 확인 후 visited 동선이랑 겹치는 지 확인
# 안 겹치면 visited에 넣고, direction 적용하여 stack에 넣는다.
# 겹치면 그대로 증발
# from collections import deque
# import sys
# input = sys.stdin.readline
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# direction = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상 하 좌 우
# change_direction_dict = {0: [0, 1, 2, 3],
#                          1: [0, 1, 3, 2],
#                          2: [1, 0, 2, 3],
#                          3: [3, 2, 1, 0],
#                          4: [2, 3, 0, 1]}
# reverse_direction_dict = {0: [0, 1, 2, 3],
#                           1: [1, 0, 2, 3],
#                           2: [0, 1, 3, 2],
#                           3: [2, 3, 0, 1],
#                           4: [3, 2, 1, 0]}
#
# current_list = []
# visited = [[set() for _ in range(M)] for _ in range(N)]
# dfs_stack = deque([])
# answer_visited = set()
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 9:
#             current_list.append((i, j))
#             answer_visited.add((i, j))
#
# for i in range(len(current_list)):
#     for j in range(4):
#         dfs_stack.append((current_list[i][0], current_list[i][1], j))
#         answer_visited.add((current_list[i][0], current_list[i][1]))
#
# while dfs_stack:
#     current = dfs_stack.pop()
#     dr = current[0] + direction[current[2]][0]
#     dc = current[1] + direction[current[2]][1]
#     if 0 <= dr < N and 0 <= dc < M:
#         if current[2] in visited[dr][dc] or arr[dr][dc] == 9:
#             continue
#         new_direction = change_direction_dict[arr[dr][dc]][current[2]]
#         reverse_direction = reverse_direction_dict[arr[dr][dc]][current[2]]
#         if arr[dr][dc] == 1 or arr[dr][dc] == 2:
#             if current[2] == reverse_direction:
#                 answer_visited.add((dr, dc))
#                 continue
#         visited[dr][dc].add(current[2])
#         visited[dr][dc].add(reverse_direction)
#         answer_visited.add((dr, dc))
#         dfs_stack.append((dr, dc, new_direction))
# print(len(answer_visited))
