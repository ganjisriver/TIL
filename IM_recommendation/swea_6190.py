TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    gop_list = []
    ind = list(map(int, input().split()))
    for i in range(N-1):
        for j in range(N-1,i,-1):
            gop_list.append(ind[i]*ind[j])

    for i in range(gop_list):



