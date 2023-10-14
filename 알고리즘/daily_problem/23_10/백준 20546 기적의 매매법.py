initial_money = int(input())
stock_money_list = list(map(int, input().split()))
junhyun_money = initial_money
junhyun_stock_cnt = 0

seongmin_money = initial_money
seongmin_stock_cnt = 0
up_flag = 0
down_flag = 0

for i in range(14):
    if junhyun_money // stock_money_list[i] >= 1:
        junhyun_stock_cnt += (junhyun_money // stock_money_list[i])
        junhyun_money -= stock_money_list[i]*(junhyun_money // stock_money_list[i])
    if i == 0:
        continue
    if stock_money_list[i-1] < stock_money_list[i]:
        up_flag += 1
        down_flag = 0
    elif stock_money_list[i-1] > stock_money_list[i]:
        up_flag = 0
        down_flag += 1
    else:
        up_flag = 0
        down_flag = 0
    if up_flag >= 3:
        seongmin_money += seongmin_stock_cnt*stock_money_list[i]
        seongmin_stock_cnt = 0
    elif down_flag >= 3:
        if seongmin_money // stock_money_list[i] >= 1:
            seongmin_stock_cnt += (seongmin_money // stock_money_list[i])
            seongmin_money -= stock_money_list[i]*(seongmin_money // stock_money_list[i])
if (seongmin_money + seongmin_stock_cnt*stock_money_list[-1]) > (junhyun_money + junhyun_stock_cnt*stock_money_list[-1]):
    print("TIMING")
elif (seongmin_money + seongmin_stock_cnt*stock_money_list[-1]) < (junhyun_money + junhyun_stock_cnt*stock_money_list[-1]):
    print("BNP")
else:
    print("SAMESAME")


