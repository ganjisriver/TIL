S = list(map(int, input().split()))
answer = 0
for i in range(len(S)):
    answer += S[i]*S[i]

answer = answer % 10
print(answer)