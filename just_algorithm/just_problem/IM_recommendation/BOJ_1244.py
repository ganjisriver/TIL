gasu = int(input())                         # 스위치 개수
matrix = list(map(int, input().split()))    # 스위치 온오프상태창
N = int(input())                            # 시행회수
                              # 성별 상태창                             # 갖게 된 번호
for i in range(N):
    S, idx = map(int, input().split())

    flag = True
    x = 1

    if S == 1:                      # 남성일때,

        while flag:
            if matrix[(idx*x)-1] == 0:
                matrix[(idx*x)-1] = 1
            elif matrix[(idx*x)-1] == 1:
                matrix[(idx*x)-1] = 0
            x += 1
            if idx*x > gasu:
                flag = False
                break
    elif S == 2:
        if matrix[idx-1] == 0:
            matrix[idx-1] = 1
        elif matrix[idx-1] == 1:
            matrix[idx-1] = 0
        while flag:
            if idx-1-x < 0 or idx-1+x >= gasu:
                flag = False
                break
            if matrix[idx-1-x] == matrix[idx-1+x]:
                if matrix[idx-1-x] == 0:
                    matrix[idx-1 - x] = 1
                    matrix[idx-1 + x] = 1
                elif matrix[idx-1-x] == 1:
                    matrix[idx-1 - x] = 0
                    matrix[idx-1 + x] = 0

            if matrix[idx-1-x] != matrix[idx-1+x]:
                flag = False
                break

            x += 1


if gasu <= 20:
    print(' '.join(map(str, matrix[:gasu])))
elif 20 < gasu <= 40:
    print(' '.join(map(str, matrix[:20])))
    print(' '.join(map(str, matrix[20:gasu])))
elif 40 < gasu <= 60:
    print(' '.join(map(str, matrix[:20])))
    print(' '.join(map(str, matrix[20:40])))
    print(' '.join(map(str, matrix[40:gasu])))
elif 60 < gasu <= 80:
    print(' '.join(map(str, matrix[:20])))
    print(' '.join(map(str, matrix[20:40])))
    print(' '.join(map(str, matrix[40:60])))
    print(' '.join(map(str, matrix[60:gasu])))
elif 80 < gasu <= 100:
    print(' '.join(map(str, matrix[:20])))
    print(' '.join(map(str, matrix[20:40])))
    print(' '.join(map(str, matrix[40:60])))
    print(' '.join(map(str, matrix[60:80])))
    print(' '.join(map(str, matrix[80:gasu])))



