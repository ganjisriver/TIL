# [모의 역량 테스트 SWEA 1952] 수영장
def counting(month, cost):
    global min_cost
    if cost > min_cost: # 이미 현재 비용이 지금 나온 최소비용보다 비싸면 추가로 돌릴필요 없이 리턴
        return

    if month <= 12:
        counting(month+1, cost+ one_list[month])  # 해당 달에서 1달 추가
        counting(month+3, cost + quater_cost)     # 해당 달에서 3달 추가

    else:
        if min_cost > cost:   # month가 12를 넘어가면 최소비용 구하는 식 시행하고 return하고 탈출
            min_cost = cost
        return
T = int(input())
for tc in range(1, T+1):
    day_cost, month_cost, quater_cost, year_cost = map(int, input().split())
    month_list = [0]+list(map(int, input().split()))    # 인덱스를 각 달로 맞추게끔 함.
    one_list = [0]*13                                   # one_day나 one_month 중 낮은 가격을 달 마다 넣을 예정
    min_cost = year_cost                                # 연간권이 최소값이면 그대로 출력되고 아니면 다른값으로 바뀔 예정

    for i in range(1, 13):                              # 1월 부터 12월 반복문 생성
        one_day_cost = day_cost*month_list[i]
        if one_day_cost > month_cost:                   # 하루권으로 한달치 사는게 한달이용권보다 비싸면
            one_list[i] = month_cost                    # 당연히 한달권을 산다.
        else:
            one_list[i] = one_day_cost                  # 하루권이 더 비싸면 하루권을 구매한다.
    counting(1, 0)                                      # 한달치와 세달치, 섞어서 하는 것의 재귀함수 출발

    print(f'#{tc} {min_cost}')
