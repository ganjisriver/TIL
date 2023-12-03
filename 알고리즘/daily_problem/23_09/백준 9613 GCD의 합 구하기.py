from itertools import combinations


def gcd(x, y):
    if y > x:
        x, y = y, x
    while y >= 1:
        x, y = y, x % y
    return x


T = int(input())
for tc in range(T):
    num_list = list(map(int, input().split()))
    answer = 0
    for x, y in combinations(num_list[1:], 2):
        answer += gcd(x, y)
    print(answer)