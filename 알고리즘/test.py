from itertools import combinations
N, M = map(int, input().split())
card_list = list(map(int, input().split()))

combi = list(combinations(card_list, 3))
answer = 0
for i in combi:
    three_hap = (i[0] + i[1] + i[2])
    if three_hap == M:
        answer = M
        break
    elif (M - three_hap) < (M - answer) and three_hap < M:
        answer = three_hap

print(answer)
