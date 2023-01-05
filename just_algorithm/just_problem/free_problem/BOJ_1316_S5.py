T = int(input())
cnt = 0
for tc in range(1, T+1):
    S = input()
    visited = []
    flag = True
    for i in range(len(S)-1):
        if S[i] in visited or S[-1] in visited:
            flag = False
            break
        if S[i] != S[i+1]:
            visited.append(S[i])

    if flag:
        cnt += 1

print(cnt)