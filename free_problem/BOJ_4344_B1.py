T = int(input())
for tc in range(1, T+1):
    score_list = list(map(int, input().split()))
    N = score_list.pop(0)
    average = 0
    cnt = 0
    for i in range(N):
        average += score_list[i]
    average = average/N
    for i in range(N):
        if score_list[i] > average:
            cnt += 1
    answer = (cnt / N)*100
    print(f'{answer:.3f}%')