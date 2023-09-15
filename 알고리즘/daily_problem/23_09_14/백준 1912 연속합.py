N = int(input())
S = list(map(int, input().split()))
for i in range(1, N):
    S[i] = max(S[i], S[i-1] + S[i])
print(max(S))