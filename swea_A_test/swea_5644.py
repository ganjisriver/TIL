# def charge(x, y, c, p):
#     x, y
#
#
# dr = [0, -1, 0, 1, 0]
# dc = [0, 0, 1, 0, -1]
#
# T = int(input())
# for tc in range(1, T+1):
#     matrix = [[0] * 10 for _ in range(10)]
#     M, A = map(int, input().split())
#     A_move = list(map(int, input().split()))
#     B_move = list(map(int, input().split()))
#     charge_list = []
#     coverage_list = []
#     performance_list = []
#     for i in range(A):
#         x, y, coverage, performance = map(int, input().split())
#         charge_list.append((x-1,y-1))
#         coverage_list.append(coverage)
#         performance_list.append(performance)
# 사용자의 위치를 업데이트하는 함수
def setNewPosistionOfUser(cur_pos, move, m_idx):
    new_y = cur_pos[0] + m_case[move[m_idx]][0]
    new_x = cur_pos[1] + m_case[move[m_idx]][1]
    # 범위 안에 들면 위치를 업데이트 하고
    if 0 < new_y < 11 and 0 < new_x < 11:
        cur_pos[0], cur_pos[1] = new_y, new_x
    # 범위 밖을 나가면 업데이트하지 않는다.
    else:
        new_y, new_x = cur_pos[0], cur_pos[1]
    return new_y, new_x


# 리스트의 최댓값과 최댓값의 위치를 반환하는 함수
def getMaxValueAndIndexOfList(lst):
    idx = -1
    max_value = 0
    for c in range(len(lst)):
        if lst[c] > max_value:
            max_value = lst[c]
            idx = c

    return max_value, idx


# 사용자의 현재 위치를 기반으로 충전받는 배터리 양의 합을 반환하는 함수
def calculate(a_pos, b_pos):
    new_a_y, new_a_x, new_b_y, new_b_x = a_pos[0], a_pos[1], b_pos[0], b_pos[1]
    cur_a_battery, cur_b_battery = [0 for _ in range(A)], [0 for _ in range(A)]

    # 각 사용자의 위치가 배터리들의 반경 안에 드는지 계산
    for a in range(A):
        battery_x, battery_y, C, P = batteries[a][0], batteries[a][1], batteries[a][2], batteries[a][3]

        if abs(new_a_y - battery_y) + abs(new_a_x - battery_x) < C + 1:
            cur_a_battery[a] = P
        if abs(new_b_y - battery_y) + abs(new_b_x - battery_x) < C + 1:
            cur_b_battery[a] = P

    # 사용자가 영향을 받는 배터리 중에서 가장 큰 충전량과 배터리의 인덱스를 가져온다.
    max_a, used_a_idx = getMaxValueAndIndexOfList(cur_a_battery)
    max_b, used_b_idx = getMaxValueAndIndexOfList(cur_b_battery)

    # 만약 충전받는 배터리의 종류가 다르다면 두 배터리 양의 합을 반환하고
    if used_a_idx != used_b_idx:
        return max_a + max_b
    # 충전받는 배터리 종류가 같다면 가장 큰 배터리 양을 제외한 최대 배터리양을 더해서 반환한다.
    else:
        cur_a_battery[used_a_idx], cur_b_battery[used_b_idx] = 0, 0
        return max_a + max(max(cur_a_battery), max(cur_b_battery))


for tc in range(int(input())):
    M, A = map(int, input().split())
    a_move, b_move = list(map(int, input().split())), list(map(int, input().split()))
    batteries = [list(map(int, input().split())) for _ in range(A)]
    m_case = [[0, 0], [-1, 0], [0, 1], [1, 0], [0, -1]]
    cur_a, cur_b = [1, 1], [10, 10]

    # 시간이 0일때 계산도 해야 됨
    sum_battery = calculate(cur_a, cur_b)
    # 시간이 지날 때마다 반복문을 돌린다.
    for m in range(M):
        # 사용자 a와 b의 새로운 위치를 구하고
        new_a_y, new_a_x = setNewPosistionOfUser(cur_a, a_move, m)
        new_b_y, new_b_x = setNewPosistionOfUser(cur_b, b_move, m)

        # 각 사용자가 배터리 반경안에 들었는지 계산하고
        # 들었다면 충전받는 배터리 양을 계산한다.
        sum_battery += calculate([new_a_y, new_a_x], [new_b_y, new_b_x])

    print('#{} {}'.format(tc + 1, sum_battery))



