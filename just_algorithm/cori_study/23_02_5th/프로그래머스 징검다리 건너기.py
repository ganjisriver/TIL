# 효율성 통과 안될 줄 알고 일단 풀어봄.
# 당연히 1차에서는 실패 뜸 NlogN으로 가야할듯

# def solution(stones, k):
#     answer = 0
#     jump = 0
#     while True:
#         for i in range(len(stones)):
#             if stones[i] > 0:
#                 jump = 0
#                 stones[i] = stones[i] - 1
#             else:
#                 jump += 1
#             if jump == k:
#                 break
#         if jump == k:
#             break
#         else:
#             answer += 1
#
#     return answer


# 2차 시도

def solution(stones, k):
    answer = 0
    chance = 9999999999999999999
    for i in range(len(stones)-k + 1):
        stones[i]
        answer_candi = 0
        for j in range(k):
            if stones[i+j] > answer_candi:
                answer_candi = stones[i+j]
    return answer

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(stones, k))