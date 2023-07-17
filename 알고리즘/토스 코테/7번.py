# N = int(input())
# num_list = list(map(int, input().split()))
# dp = [1]*N
# for i in range(N):
#     for j in range(i):
#         if num_list[j] < num_list[i]:
#             dp[i] = max(dp[i], dp[j]+1)
# print(max(dp))

def solution(schedules):
    size = len(schedules)
    if size == 1:
        return schedules[0]

    table = [0 for _ in range(size)]
    table[0] = schedules[0]
    table[1] = schedules[1]

    for i in range(2, size):
        table[i] = max(table[i - 2] + schedules[i], table[i - 1])
    answer = table[size - 1]
    return answer
print(solution([30, 90, 30, 30, 30, 75, 75]))
print(solution(
[15, 45, 90, 15, 90, 60]))
print(solution([30, 30, 60, 90, 60, 15, 15, 60]))
print(solution([45, 15, 30]))