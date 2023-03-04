def solution(grid):
    rl = len(grid)
    cl = len(grid[0])
    left_dict = {1:3, 2:4, 3:2, 4:1}
    right_dict = {1:4, 2:3, 3:2, 4:1}
    dr = [0, -1, 1, 0, 0]
    dc = [0, 0, 0, -1, 1]
    answer = []
    dict_setting = dict()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            dict_setting[(i, j)] = []

    for i in range(1, 5):
        x, y = 0
        while True:
            dx = x + dr
            dy = y + dc
            if grid[i][j] == 'L':

            elif grid[i][j] == 'R':

            else:

            for i in range(len(dict_setting[(x, y)])):
                if dict_setting[(x,y)][i] =


    return dict_setting

grid1 = ["SL", "LR"]
grid2 = ["S"]
grid3 = ["R", "R"]
print(solution(grid1))
