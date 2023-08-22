# N = int(input())
# dp = [0, 1]
#
# for i in range(2, N+1):
#     min_value = 999999999999
#     j = 1
#     while (j**2) <= i:
#         min_value = min(min_value, dp[i - (j**2)])
#         j += 1
#     dp.append(min_value+1)
# print(dp[N])

from itertools import combinations_with_replacement
N = int(input())
squares_list = [i**2 for i in range(224)]
squares_set = set(squares_list)
if N in squares_set:
    print(1)
    exit(0)
squares_list_2 = [sum(j) for j in combinations_with_replacement(squares_list, 2)]
squares_2_set = set(squares_list_2)
if N in squares_2_set:
    print(2)
    exit(0)
for i in squares_list:
    if (N - i) in squares_2_set:
        print(3)
        exit(0)
print(4)