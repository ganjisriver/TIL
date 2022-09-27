from collections import deque
def rotations(idx, direction):
    first_gear, second_gear, third_gear, fourth_gear = magnet[0], magnet[1], magnet[2], magnet[3]
    if idx == 0:
        if first_gear[2] != second_gear[6]:
            if second_gear[2] != third_gear[6]:
                if third_gear[2] != fourth_gear[6]:
                    fourth_gear.rotate(-direction)
                third_gear.rotate(direction)
            second_gear.rotate(-direction)
        first_gear.rotate(direction)

    if idx == 1:
        if second_gear[6] != first_gear[2]:
            first_gear.rotate(-direction)
        if second_gear[2] != third_gear[6]:
            if third_gear[2] != fourth_gear[6]:
                fourth_gear.rotate(direction)
            third_gear.rotate(-direction)
        second_gear.rotate(direction)
    if idx == 2:
        if third_gear[2] != fourth_gear[6]:
            fourth_gear.rotate(-direction)
        if third_gear[6] != second_gear[2]:
            if second_gear[6] != first_gear[2]:
                first_gear.rotate(direction)
            second_gear.rotate(-direction)
        third_gear.rotate(direction)
    if idx == 3:
        if third_gear[2] != fourth_gear[6]:
            if second_gear[2] != third_gear[6]:
                if first_gear[2] != second_gear[6]:
                    first_gear.rotate(-direction)
                second_gear.rotate(direction)
            third_gear.rotate(-direction)
        fourth_gear.rotate(direction)
    magnet[0], magnet[1], magnet[2], magnet[3] = first_gear, second_gear, third_gear, fourth_gear
    return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    magnet = [deque(list(map(int, input().split()))) for _ in range(4)]
    for _ in range(N):
        a, b = map(int, input().split())
        rotations(a-1, b)
    answer = 0
    if magnet[0][0]:
        answer += 1
    if magnet[1][0]:
        answer += 2
    if magnet[2][0]:
        answer += 4
    if magnet[3][0]:
        answer += 8

    print(f'#{tc} {answer}')



