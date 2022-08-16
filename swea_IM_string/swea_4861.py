TC = int(input())                               # 테스트케이스 회수
for tc in range(1, TC+1):
    N, M = map(int, input().split())            # N은 정사각형 한변의 길이, M은 회문의 길이
    matrix = [input() for _ in range(N)]        # 숫자열 N개의 리스트 만들기

    result = []                                 # 결과값을 출력하기 위한 빈 리스트 생성

    # 가로행 구하기
    for r in range(N):
        for c in range(N-M+1):
            if matrix[r][c:c+M] == matrix[r][c:c+M][::-1]: # M만큼 길이의 문자열을 뒤에서 출력해도 같으면 회문
                result.append(matrix[r][c:c+M])            # 그 회문 값을 result에 넣어줌

    # 세로행 구하기
    for r in range(N-M+1):
        for c in range(N):
            C_list = []                                 # 세로행에 넣기 위한 리스트 구하기
            for i in range(M):
                C_list.append(''.join(matrix[r+i][c]))  # 세로는 슬라이싱이 힘들기 때문에, 반복문을 한번더 써서 세로행을 C_list에 넣어준다.
            if C_list == C_list[::-1]:                  # 마찬가지로 리스트와 리스트의 역출력값과 같으면 회문
                result.append(''.join(C_list))          # 회문이면 result 리스트에 문자열로 넣어준다.
    res = ''.join(result)
    print('#{} {}'.format(tc, res))




