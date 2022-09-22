T = int(input())
for tc in range(1, T+1):
    N = int(input())
    train_list = []
    cnt = 1
    for _ in range(N):
        start, end = map(int, input().split())
        train_list.append((start, end))
    train_list.sort(key=lambda x: x[1])
    start, end = train_list.pop(0)
    while train_list:
        if end <= train_list[0][0]:
            start, end = train_list.pop(0)
            cnt += 1
        else:
            train_list.pop(0)
    print(f'#{tc} {cnt}')

