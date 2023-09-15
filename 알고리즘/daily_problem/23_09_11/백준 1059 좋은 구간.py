from itertools import combinations
N = int(input())
S = list(map(int, input().split()))
n = int(input())

S.sort()
min_value = 0
max_value = 0
flag = False
for i in range(1, N):
    if S[i-1] < n < S[i]:
        min_value = S[i-1]
        max_value = S[i]
        flag = True
        break
    elif n < S[0] and S[0] > 1:
        flag = True
        min_value = 0
        max_value = S[0]
if not flag:
    print(0)
else:
    cnt = 0
    for a, b in combinations(range(min_value+1, max_value), 2):
        if a <= n <= b:
            cnt += 1
    print(cnt)