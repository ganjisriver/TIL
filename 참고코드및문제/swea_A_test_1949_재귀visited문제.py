# 재귀에서 visited값을 재귀로 넣어주는데, set으로 만든 visited 값을 새롭게 set으로 묶어줌으로써, id값 겹치는 것을 방지함.
# 굉장히 중요한 부분인듯.
T = int(input())


def road_finder(r, c, elevation, distance, visited, is_carved):
    global answer
    visited = set(visited)  # id 값 새로 파줘야 그다음 재귀 단계에서 걸리지 않음.
    visited.add((r, c))

    if answer < distance:
        answer = distance

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >= N or nc < 0 or nc >= N or (nr, nc) in visited:
            continue

        if is_carved:  # 이전 단계에서 이미 깎을 기회를 썼던 경우라면?
            if trails[nr][nc] < elevation:  # 그냥 가보는거 외엔 할 수 있는 게 없음
                road_finder(nr, nc, trails[nr][nc], distance+1, visited, True)  # 깎였음을 표시 여전히 유지

        else:  # 깎을 기회가 남아있는 경우라면?
            if trails[nr][nc] < elevation:  # 그냥 가보거나
                road_finder(nr, nc, trails[nr][nc], distance + 1, visited, False)

            for k in range(K, 0, -1):  # K 를 하나씩 줄여 가면서?
                if trails[nr][nc] - k < elevation:  # 깎은 상태로 가본다
                    road_finder(nr, nc, trails[nr][nc] - k, distance + 1, visited, True)  # 깎였다고 표시


for tc in range(1, T + 1):
    N, K = map(int, input().split())  # N * N 행렬과, K 최대공사 가능 깊이
    trails = [list(map(int, input().split())) for _ in range(N)]
    highest = 0
    start_points = []

    for a in range(N):  # 일단 제일 높은 봉우리 골라내고
        for b in range(N):
            if trails[a][b] > highest:
                highest = trails[a][b]

    for x in range(N):  # 해당 봉우리가 가장 높다면 좌표를 찾아내준다
        for y in range(N):
            if trails[x][y] == highest:
                start_points.append((x, y))

    dr = [-1, 1, 0, 0]  # 대충 4방향
    dc = [0, 0, 1, -1]
    answer = 0

    for (r, c) in start_points:  # 하나에 해당하는 봉우리 시작점에 대해
        road_finder(r, c, highest, 1, set(), False)  # 길찾기 시작

    print('#{} {}'.format(tc, answer))