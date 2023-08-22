from collections import deque
from copy import deepcopy
direction = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
def binary_visited(board):
    binary_str = ""
    for x in range(3):
        for y in range(3):
            binary_str += "0" if board[x][y] == "." else "1"
    return int(binary_str, 2)

def bfs(board):
    time = 0
    init_board = [['.' for _ in range(3)] for _ in range(3)]
    q = deque([init_board])
    visited = [0 for _ in range(1025)]
    visited[binary_visited(init_board)] = 1
    while q:
        for i in range(len(q)):
            current_board = q.popleft()
            if board == current_board:
                return time

            for x in range(3):
                for y in range(3):
                    new_board = deepcopy(current_board)
                    for direct in range(5):
                        dx, dy = x + direction[direct][0], y + direction[direct][1]
                        if 0 <= dx < 3 and 0 <= dy < 3:
                            new_board[dx][dy] = "*" if new_board[dx][dy] == '.' else '.'
                    visited_code = binary_visited(new_board)
                    if not visited[visited_code]:
                        q.append(new_board)
                        visited[visited_code] = 1
        time += 1

T = int(input())
for tc in range(T):
    test_board = []
    for _ in range(3):
        test_board.append(list(input()))
    answer = bfs(test_board)
    print(answer)





