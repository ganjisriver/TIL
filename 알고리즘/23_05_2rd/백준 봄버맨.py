direction = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]

R, C, N = map(int, input().split())
first_bomb_set = set()
full_bomb_board = [['O']*C for _ in range(R)]
# print(full_bomb_board)
board = []
for i in range(R):
    board_item_list = list(input())
    board.append(board_item_list)
    for j in range(C):
        if board_item_list[j] == "O":
            first_bomb_set.add((i, j))

if N == 1:
    for i in range(R):
        line = ""
        for j in range(C):
            line += board[i][j]
        print(line)
else:
    if N % 4 == 1:
        pass
    elif N % 2 == 0:
        for i in range(R):
            print('O'*C)
    elif N % 4 == 3:
        for i in range(len(first_bomb_set)):
            r, c = first_bomb_set.pop()
            for j in range(5):
                dr = r + direction[j][0]
                dc = c + direction[j][1]
                if dr < 0 or dr >= R or dc < 0 or dc >= C:
                    continue
                else:
                    full_bomb_board[dr][dc] = '.'
        for i in range(R):
            print("".join(full_bomb_board[i]))



