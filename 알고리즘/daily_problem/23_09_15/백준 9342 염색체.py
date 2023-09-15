
T = int(input())
for tc in range(T):
    S_set = {"A", "B", "C", "D", 'E', "F"}
    flag = True
    A_is = False
    F_is = False
    C_is = False
    Last_is = True
    S = input()
    for i in range(len(S)):
        if i != len(S)-1 and A_is and C_is and F_is:
            flag = False
            break
        if S[-1] not in S_set:
            flag = False
            break
        if i == 0:
            if S[i] not in S_set:
                flag = False
                break
            if S[i] == "A":
                A_is = True

        else:
            if S[i] == "A":
                A_is = True
            elif S[i] == "F":
                if A_is:
                    F_is = True
                elif A_is and C_is and not F_is:
                    flag = False
                    break
                else:
                    flag = False
                    break
            elif S[i] == "C":
                if A_is and F_is:
                    C_is = True
                else:
                    flag = False
                    break

    if flag:
        print("Infected!")
    else:
        print("Good")

