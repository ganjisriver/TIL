TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    C_list = list(map(int, input().split()))

    q = []
    flag = True
    cnt = 0
    while flag:

        for k in range(N):
            q.append(C_list[((k + cnt) & M)])

        for k in range(N):
            q[0] // 2
            C_list[((k + cnt) & M)] = q.pop(0)



            if q.pop(0) == 0:





        i += 1
        cnt += N
        for _ in range(M):
            if C_list[_] == 0:
                flag = False
                break




