TC = int(input())
for tc in range(1, TC+1):
    N = list(map(int, input().split()))
    is_sum_zero = 0
    for i in range(1, 1<< len(N)):
        sub_list = []
        for j in range(len(N)):
            if i & (1<< j):
                sub_list.append(N[j])

        total = 0

        for num in sub_list:
            total += num

            if total == 0:
                is_sum_zero = 1
                break


    print(f'#{tc} {is_sum_zero}')

