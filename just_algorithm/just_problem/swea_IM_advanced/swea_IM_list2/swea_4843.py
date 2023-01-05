TC = int(input())
for tc in range(1, TC + 1):
    length = int(input())
    total_list = list(map(int, input().split()))
    min_list = []
    max_list = []
    sorted_list = []

    total_list.sort()

    for idx in range(int(length / 2)):
        min_list.append(total_list[idx])
    for idx in range(int(length / 2), length):
        max_list.append(total_list[idx])
    max_list.sort(reverse=True)

    for i in range(length):
        if i % 2 == 0:
            sorted_list.append(max_list[int(i / 2)])
        elif i % 2 == 1:
            sorted_list.append(min_list[int(i / 2)])
    print(f'#{tc}', end=' ')
    for i in range(10):
        print(sorted_list[i], end=' ')
    print()
