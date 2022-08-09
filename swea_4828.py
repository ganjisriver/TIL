tc_num = int(input())                       # 테스트 케이스 넣기
for i in range(1, tc_num+1):                # 테스트 케이스만큼 돌리기
    n = int(input())                        # 리스트로 받는 값의 개수
    max_value = 0                           # 최대값 변수 설정
    min_value = 1000001                     # 최소값 변수 설정
    num = list(map(int, input().split()))   # 리스트 입력값 받기
    for j in num:                           # 최대값 받기
        if j > max_value:
            max_value = j
        
        if j < min_value:                   # 최소값 받기
            min_value = j
    print(f'#{i} {max_value - min_value}')  # 최대값 - 최소값
    