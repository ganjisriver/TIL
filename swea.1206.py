# 테스트 10번 진행
for t in range(1, 11): 
    num = int(input()) # 빌딩 개수
    
    # 빌딩 높이 리스트
    height = list(map(int, input().split()))
    
    cnt_num = 0 # 조망권 확보 세대 숫자를 세기위한 변수설정
    
    # 맨 왼쪽 두칸, 맨 오른쪽 두칸 제외한 건물
    for i in range(2, num-2):
        # 건물 왼쪽, 오른쪽 2칸보다 높은 i찾기(조망권 확보한 건물)
        if height[i] > height[i-2] and height[i] > height[i-1] and height[i] > height[i+1] and height[i] > height[i+2]:
            
            # i번째 건물을 제외하고 가장 높은 건물을 찾기 위한 변수 설정
            high_height = 0
            
            for j in range(-2, 3):
                
                # 0을 가장 높은 건물로 설정하고, 그 다음 높은 건물을 찾는 것이기 때문에, j==0은 조건제외
                if j==0:
                    continue
                #나머지 4개의 건물중 가장 높은 층수 구하기
                if height[i+j] > high_height:

                    high_height = height[i+j]
            
            cnt_num += height[i] - high_height
    
    print(f'#{t} {cnt_num}')