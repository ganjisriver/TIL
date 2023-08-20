def solution(sticker):
    size = len(sticker)
    if size == 1: return sticker[0]

    table = [[0 for _ in range(size)] for _ in range(2)]
    table[0][0] = sticker[0]
    table[0][1] = sticker[0]
    table[1][1] = sticker[1]

    for i in range(2, size - 1): table[0][i] = max(table[0][i - 2] + sticker[i], table[0][i - 1])
    for i in range(2, size): table[1][i] = max(table[1][i - 2] + sticker[i], table[1][i - 1])
    answer = max(table[0][size - 2], table[1][size - 1])
    return answer

sticker1 = [14, 6, 5, 11, 3, 9, 2, 10]
sticker2 = [1, 3, 2, 5, 4]

print(solution(sticker1))
print(solution(sticker2))