test_num = int(input()) # 테스트 회수
for n in range(1, test_num+1): # 테스트 회수만큼 돌리기 위한 for문
    value = input() # 각 테스트의 입력값
    
    cnt = [0]*10    # value값의 숫자들을 cnt에 입력할 예정
    for num in value:
        cnt[num] += 1
idx = 0
    if cnt[idx] >= 3:
        cnt[idx] -= 3
        is_babysin += 1
        continue
    
    if idx < 8: