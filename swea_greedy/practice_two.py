TC = int(input())
for tc in range(1, TC+1):
    babygin_idx =[0]*10
    cards = input()

    for i in range(len(cards)):
        babygin_idx[int(cards[i])] += 1
    babygin = 0
    i = 0
    while i <= 9:
        if babygin_idx[i] == 6:
            babygin += 2
            break
        if babygin_idx[i] == 3:
            babygin += 1
            babygin_idx[i] -= 3


        if i <= 7:
            if babygin_idx[i] and babygin_idx[i+1] and babygin_idx[i+2]:
                babygin += 1
                babygin_idx[i] -= 1
                babygin_idx[i + 1] -= 1
                babygin_idx[i + 2] -= 1
        i += 1

    if babygin == 2:
        print('True')
    else:
        print('False')