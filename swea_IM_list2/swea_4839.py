TC = int(input())
for tc in range(1, TC+1):
    P, A, B = map(int, input().split())

    left_A = 1
    right_A = P
    left_B = 1
    right_B = P
    c_A, c_B = int((left_A+right_A)/2), int((left_B+right_B)/2)

    while True:
        if A == c_A and B == c_B:
            print(f'#{tc} {0}')
            break
        elif A == c_A:
            print(f'#{tc} A')
            break

        elif B == c_B:
            print(f'#{tc} B')
            break

        if A > c_A:
            left_A = c_A
            c_A = int((left_A+right_A) / 2)
        elif A < c_A:
            right_A = c_A
            c_A = int((left_A+right_A) / 2)

        if B > c_B:
            left_B = c_B
            c_B = int((left_B+right_B) / 2)
        elif B < c_B:
            right_B = c_B
            c_B = int((left_B+right_B) / 2)





