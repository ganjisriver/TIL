def solution(grid):
    dr = [0, -1, 1, 0, 0]
    dc = [0, 0, 0, -1, 1]
    answer = []
    dict_setting = dict()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            dict_setting[(i, j)] = []

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            visited_dict = dict_setting
            for k in range(1, 5):
                starting_point = grid[i][j]
                while True:




    answer.sort(reverse=True)
    return dict_setting

grid1 = ["SL", "LR"]
grid2 = ["S"]
grid3 = ["R", "R"]
print(solution(grid1))
