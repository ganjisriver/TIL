import sys
sys.setrecursionlimit(10**6)

def dice_back(idx):
    if idx == 0:
        reverse_idx = 5
    elif idx == 1:
        reverse_idx = 3
    elif idx == 2:
        reverse_idx = 4
    elif idx == 3:
        reverse_idx = 1
    elif idx == 4:
        reverse_idx = 2
    elif idx == 5:
        reverse_idx = 0

    return reverse_idx


def counting(depth, idx, sum_value):
    global max_value
    next_idx_back = 0
    if depth == N-1:
        idx_back = dice_back(idx)
        A = dice[depth][:]
        A[idx] = 0
        A[idx_back] = 0
        max_dice = max(A)
        if max_value < sum_value + max_dice:
            max_value = sum_value + max_dice
        return

    for j in range(6):
        if dice[depth][idx] == dice[depth+1][j]:
           next_idx_back = j
    next_idx = dice_back(next_idx_back)
    idx_back = dice_back(idx)
    A = dice[depth][:]
    A[idx] = 0
    A[idx_back] = 0
    max_dice = max(A)

    counting(depth+1, next_idx, sum_value + max_dice)

N = int(input())
dice = [list(map(int, input().split())) for _ in range(N)]
# idx = 0 5 / 1 3 / 2 4
max_value = 0
for i in range(6):
    counting(0, i, 0)
print(max_value)
