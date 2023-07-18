# N = int(input())
# character_list = [0]+ list(map(int ,input().split()))
# power_list = [0] + list(map(int, input().split()))
# day = int(input())
# day_dp = [[0]*(N+1) for _ in range(day+1)]
# day_dp[0] = [power_list[i]*character_list[i] for i in range(N+1)]
# print(day_dp)
#자두나무
# i 시간의 흐름
# j 움직인 회수
# k 현재 위치

# i는 시간이 흐름
# j는 훈련 시킬 캐릭터의 레벨
# k는 당장 레벨업 가능한 수 -> ?이게 의미가 ㅣㅆ나
# 하루 걸러서 레벨업을 했다. 그렇다면 dp[i][j][k] = dp[i-k][j+1][k] + (power_list[j+1] - power_list[j])*k
# for i in range(1, day+1):
# dp[1][1][1] = dp[0][2][
import sys

INF = float('inf')


def get_dp(current_day, current_character, left_chance):
    if current_character == n - 1:
        return 0
    if dp[current_day][current_character][left_chance] != -1:
        return dp[current_day][current_character][left_chance]

    ret = 0
    for i in range(left_chance + character_list[current_character] + 1):
        if current_day < i:
            break
        ret = max(ret, get_dp(current_day - i, current_character + 1, i) + (power[current_character + 1] - power[current_character]) * i)

    dp[current_day][current_character][left_chance] = ret
    return ret


n = int(input())
character_list = list(map(int, input().split()))
power = list(map(int, input().split()))
day = int(input())

result = sum(character_list[i] * power[i] for i in range(n))
# print(result)
dp = [[[-1] * 105 for _ in range(n+1)] for _ in range(105)]

print(result + get_dp(day, 0, 0))