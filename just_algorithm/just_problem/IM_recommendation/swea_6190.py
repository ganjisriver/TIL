TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    ind = list(map(int, input().split()))
    gop_list = []
    danjo = []
    max_value = 0
    for i in range(N-1):
        for j in range(i+1, N):
            gop_list.append(str(ind[i]*ind[j]))

    for i in range(len(gop_list)):
        flag = True
        for j in range(len(gop_list[i])-1):
            if not int(gop_list[i][j]) <= int(gop_list[i][j+1]):
                flag = False
                break
            else:
                pass
        if flag:
            danjo.append(int(gop_list[i]))




    for i in range(len(danjo)):
        if max_value < danjo[i]:
            max_value = danjo[i]
    if len(danjo) == 0:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {max_value}')




