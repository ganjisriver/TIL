for tc in range(1, 11):
    TC = int(input())
    finding_string = input()
    whole_string = input()
    a = list(map(str, whole_string))
    N = len(a)
    idx = -1
    cnt = 0
    while True:
        idx = whole_string.find(finding_string, idx+1, N)
        if idx == -1:
            break
        cnt += 1
    print(f'#{tc} {cnt}')





