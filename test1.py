#  이곳에 코드와 주석을 작성합니다.

T = int(input())                                # 테스트 횟수 입력

for t in range(1, T+1):                         # 테스트 횟수 진행
    N = int(input())                            # 입력받을 카드의 장수
    card_list = list(map(int, input()))         # 입력받은 카드를 각 요소로 분리하여 리스트에 저장
    cnt_list = [0] * 10                         # 카드의 장수를 저장할 리스트 생성

    for card_num in card_list:                  # 특정 숫자의 카드가 나올 때마다, '해당 숫자 카드 장수 + 1' 씩 증가
        cnt_list[card_num] += 1

    max_card = 0                                # 최대 크기를 갖는 카드
    how_many = 0                                # max_card의 장수

    for idx in range(10):                       # cnt_list 순회
        if cnt_list[idx] == 0:                  # 카드가 없는 경우, 다음 카드로 넘어감
            continue

        else:                                   # 카드가 있는 경우, 하기 알고리즘 진행
            if how_many <= cnt_list[idx]:
                how_many = cnt_list[idx]        # '최대 장수' 가 나올 때마다 업데이트
                max_card = idx                  # '최대 장수'를 갖는 '카드의 값' 업데이트

    print(f'#{t} {max_card} {how_many}')