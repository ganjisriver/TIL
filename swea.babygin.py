import sys
sys.stdin = open('input(1).txt')

test_num = int(input()) # 테스트 회수
for n in range(1, test_num+1): # 테스트 회수만큼 돌리기 위한 for문
    value = input() # 각 테스트의 입력값
    
    cnt = [0]*10    # value값의 숫자들을 cnt에 입력할 예정
    for num in value:
        cnt[num] += 1
    idx = 0
    is_babysin = 0
    for i in range(10):
        if cnt[i] >=3:
            cnt[i] -= 3
            is_babysin +=1
        
        if cnt[i-1] == 1 and cnt[i] ==1 and cnt[i+1] == 1:
            is_babysin += 1
            cnt[i-1] -=1 
            cnt[i] -= 1 
            cnt[i+1] -= 1
            

    
    if is_babysin == 2:
        print(f'#{n} {1}')
    else:
        print(f'#{n} {0}')