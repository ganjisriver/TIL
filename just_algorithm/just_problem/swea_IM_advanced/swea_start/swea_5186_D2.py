TC = int(input())               # 테스트케이스 회수
for tc in range(1, TC+1):
    N = float(input())          # 이진수로 나타낼 값 실수형으로 받기
    result = str()              # 이진수 값 받을 문자형 변수 지정

    for i in range(1, 13):      # 이진수가 12이상 나타날시 overflow하면 되니까 12번까지 돌려줌
        if N < 2**-i:           # N은 이진수들의 합이기 때문에, 자리값들을 모두 확인해 줄예정
            result += '0'       # 받은 값이 2**-i값보다 작으면 0찍고 다른 자리값이랑 비교할 예정
        elif N >= 2**-i:        # N이 2**-i보다 크면 그 자리는 무조건 1을 찍어줌
            N -= 2**-i          # result에 값을 나타내줬으니 N에서 그 값을 빼줌
            result += '1'       # 지속적으로 돌려줄 예정

        if N == 0:              # N이 0이 될 때, 각 자리에 맞는 값 배정 완료 break걸어줘도됨
            break
    if N == 0:                  # N이 0이면 그냥 이진수값 표현한거 출력해주면됨.
        print(f'#{tc} {result}')
    else:                       # 12번 돌릴 때 까지 N이 0이 아니면 뒤에 자리수가 남아있는거니까 overflow출력해줌
        print(f'#{tc} overflow')





