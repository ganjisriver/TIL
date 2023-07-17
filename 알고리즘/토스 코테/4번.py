import heapq
def solution(prices, k):
    answer = -1
    for i in range(len(prices)):
        current_buying = prices[i]
        cnt_list = []
        answer_candi = 0
        for j in range(i, len(prices)):
            if current_buying < prices[j]:
                cnt_list.append(-prices[j])
        if len(cnt_list) >= k:
            heapq.heapify(cnt_list)
            for j in range(k):
                answer_candi -= (heapq.heappop(cnt_list) + current_buying)
            if answer < answer_candi:
                answer = answer_candi

    return answer

print(solution(
[10, 7, 8, 5, 8, 7, 6, 2, 9], 3))
print(solution(
[10, 8, 6, 5, 7, 6, 4, 2, 1], 4))
print(solution([10, 6, 5, 6, 7, 4, 3, 1, 10], 3))
print(solution([44, 51, 44, 47, 47, 43, 40, 36, 35, 35, 30], 3))
print(solution([77, 89, 81, 75, 66, 73, 85, 89], 3))
