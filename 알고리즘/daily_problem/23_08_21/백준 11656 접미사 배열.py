S = input()
S_list = sorted([S[i:] for i in range(len(S))])
for i in range(len(S_list)):
    print(S_list[i])