T = int(input())
for tc in range(1, T+1):
    N, K_min, K_max = map(int, input().split())
    score_list = list(map(int, input().split()))
    T1 = 0
    T2 = 0
    min_value = 100000000
    max_score = max(score_list)

    for i in range(max_score):
        for j in range(i+1, max_score+1):
            T1 = i
            T2 = j
            class_number_list = []
            A_class = []
            B_class = []
            C_class = []
            for k in range(len(score_list)):
                if score_list[k] >= T2:
                    A_class.append(score_list[k])
                elif T1 <= score_list[k] < T2:
                    B_class.append(score_list[k])
                elif score_list[k] < T1:
                    C_class.append(score_list[k])

            if K_min <= len(A_class) <= K_max and K_min <= len(B_class) <= K_max and K_min <= len(C_class) <= K_max:
                class_number_list.append(len(A_class))
                class_number_list.append(len(B_class))
                class_number_list.append(len(C_class))
                if min_value > (max(class_number_list) - min(class_number_list)):
                    min_value = (max(class_number_list) - min(class_number_list))
            else:
                continue

    if min_value == 100000000:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {min_value}')