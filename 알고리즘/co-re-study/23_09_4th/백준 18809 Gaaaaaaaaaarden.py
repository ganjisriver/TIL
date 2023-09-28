from itertools import combinations
N, M, G, R = map(int, input().split())
garden = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
ground_list = []

for i in range(N):
    for j in range(M):
        if garden[i][j] == 2:
            ground_list.append((i, j))


# 빨강, 초록의 순서 및 빈 배양액 땅까지 고려하는 경우를 모두 구해야 함.
