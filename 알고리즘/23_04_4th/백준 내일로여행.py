'''
내일로 혜택 - 무궁화호, ITX 무료 + S-Train, V-Train 50% 할인
내일로 티켓을 사는 것이 이득인지 아닌지 계산
'''

# 첫째 줄: 한국의 도시의 수, 내일로 티켓 값
# 둘째 줄: 도시의 이름
# 셋째 줄: 여행할 도시의 수
# 넷째 줄: 여행할 도시의 이름
# 다섯째 줄: 교통수단의 수
# 여섯째 줄부터: 교통수단의 종류, 가격

kr_city_num, nailo_price = map(int, input().split())
kr_cities = list(input().split())
travel_city_num = int(input())
travel_cities = list(map(input().split()))
trans_num = int(input())
transform_list = []
for i in range(trans_num):
    transform = list(input().split())
    transform_list.append(transform)
