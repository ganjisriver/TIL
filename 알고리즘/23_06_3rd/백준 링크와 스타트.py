from itertools import combinations
import sys
input = sys.stdin.readline
N = int(input())
arr = []
team_numbers_list = []
start_team_member_list = []
link_team_member_list = []
order_list = [i+1 for i in range(N)]

score_list = [list(map(int, input.split())) for _ in range(N)]
for i in range(2, N):
    first, second = i, N-i
    if first > second:
        break
    else:
        team_numbers_list.append(first)

for first in team_numbers_list:
    order_combi_list = list(combinations(order_list, first))
    res = 99999999999999
    for t in range(len(order_combi_list)):
        order_combi_list[t] = set(order_combi_list[t])
        start_power = 0
        link_power = 0
        for i in range(N//2):
            for j in range(N//2):
                if i in order_combi_list[t] and j in order_combi_list[t]:
                    start_power += arr[i][j]
                elif i not in order_combi_list[t] and j not in order_combi_list[t]:
                    link_power += arr[i][j]
        if res > abs(start_power - link_power):
            res = abs(start_power - link_power)
        if res == 0:
            break
print(res)


