from collections import deque
#deque 슬라이싱 안됨.

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    password = list(input())
    number_list = []
    real_number_list = []
    for i in range(N//4):
        password = deque(password)
        password.rotate(1)
        password = list(password)
        for j in range(0, N, N//4):
            temp = password[j:(j+N//4)]
            number = ''.join(temp)
            number_list.append(number)
    for i in range(len(number_list)):
        ten_number = int(number_list[i], 16)
        real_number_list.append(ten_number)
    real_number_list = set(real_number_list)
    real_number_list = list(real_number_list)
    real_number_list.sort(reverse=True)
    answer = real_number_list[K-1]
    print(f'#{tc} {answer}')




