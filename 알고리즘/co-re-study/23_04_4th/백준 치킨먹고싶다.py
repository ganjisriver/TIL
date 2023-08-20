import sys


# 이게 왜 안되는지 이해가 안돼서 곤란하다.
T = int(sys.stdin.readline())

for i in range(T):
    chicken_price, total_money, required_coupons, given_coupon = map(int, sys.stdin.readline().split())
    total_chicken_orders = total_money // chicken_price
    more_chicken_coupon = total_chicken_orders // required_coupons*given_coupon
    answer = more_chicken_coupon*given_coupon // required_coupons
print(answer)



