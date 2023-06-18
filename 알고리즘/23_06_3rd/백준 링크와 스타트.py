from itertools import combinations
N = int(input())
arr = []
team_numbers_list = []
start_team_member_list = []
link_team_member_list = []
order_list = [i+1 for i in range(N)]

for i in range(N):
    score_list = list(map(int, input().split()))
    arr.append(score_list)
for i in range(2, N):
    first, second = i, N-i
    if first > second:
        break
    else:
        team_numbers_list.append((first, second))

for first, second in team_numbers_list:
    

order_combi_list = list(combinations(order_list, 3))
for i in range(len(order_combi_list)):
    order_combi_list[i] = set(order_combi_list[i])
