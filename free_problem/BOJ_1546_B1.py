N = int(input())
score_list = list(map(int, input().split()))
max_score = max(score_list)
for i in range(N):
    score_list[i] = score_list[i]/max_score*100
average = 0
for i in range(N):
    average += score_list[i]
average = average/N

print(average)