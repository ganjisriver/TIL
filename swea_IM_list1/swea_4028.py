tc_num = int(input())
for i in range(1, tc_num + 1):
    n = int(input())
    max_value = 0
    min_value = 1000001
    num = list(map(int, input().split()))
    for j in num:
        if j > max_value:
            max_value = j

        if j < min_value:
            min_value = j
    print(f'#{i} {max_value - min_value}')

