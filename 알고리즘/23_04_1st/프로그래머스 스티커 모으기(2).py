def solution(sticker):
    answer = 0
    sticker_lenth = len(sticker)
    if sticker_lenth == 1:
        return sticker[0]

    stikcer_dp = [[0 for _ in range(sticker_lenth)] for _ in range(2)]
    for i in range(2, len(sticker)):
        off_sticker = 0

    return answer

sticker1 = [14, 6, 5, 11, 3, 9, 2, 10]
sticker2 = [1, 3, 2, 5, 4]

print(solution(sticker1))
print(solution(sticker2))