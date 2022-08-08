test_num = int(input()) # 총 테스트 회수
for tc in range(1, int(test_num+1):
    box_line = int(input()) # 상자열의 개수
    
    test_value = list(map(int, input().split())) # 각 열의 상자의 개수 
    
    max_value = 0 # 낙차가 가장 큰 열을 구하기 위한 변수

    for i in range(box_line): # 각각의 상자열을 보기위한 for문
        cnt = 0 # i열에서 나올 수 있는 가장 큰 낙차
        
        for j in range(i+1, box_line): # i+1은 그 이전꺼는 비교를 하지 않아도 된는 의미
            if tc[i] > tc[j]: # j열의 상자 개수가 i열보다 작아야 낙차가 1개씩 늘어남. 
                cnt += 1

        if cnt > max_value: # 각자 열의 낙차를 비교해서 가장 높은 열의 낙차를 max_value로 넣게 된다. 
            max_value = cnt

    print(f'#{tc} {max_value}')