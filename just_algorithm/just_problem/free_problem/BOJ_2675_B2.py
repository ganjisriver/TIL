T = int(input())
for tc in range(1, T+1):
    R, S = input().split()
    R = int(R)
    ans = str()
    for i in range(len(S)):
        ans += S[i]*R
    print(ans)
