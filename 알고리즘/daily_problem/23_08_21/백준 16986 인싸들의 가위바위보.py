from itertools import permutations

def DFS(player1, player2, index, win_list, players):
    global result
    if win_list[0] == K:
        result = 1
        return
    if win_list[1] == K or win_list[2] == K:
        return
    if index[0] == N:
        return
    player3 = 3 - (player1 + player2)  # 이전 출전했던 선수들의 합을 3에서 빼면 다음출전할 선수->player3
    pv1 = players[player1][index[player1]] - 1  # player1이 낼 손모양 -> 손모양 인덱스는 0부터니까 1빼주기
    pv2 = players[player2][index[player2]] - 1
    index[player1] += 1  # player1 한번 냈으니까, 인덱스 증가 -> 다음에 낼 손모양 결정
    index[player2] += 1
    if relations[pv1][pv2] == 2 or (relations[pv1][pv2] == 1 and player1 > player2):  # player1이 이긴 경우
        win_list[player1] += 1
        DFS(player1, player3, index, win_list, players)
    elif relations[pv1][pv2] == 0 or (relations[pv1][pv2] == 1 and player1 < player2):  # player2가 이긴 경우
        win_list[player2] += 1
        DFS(player2, player3, index, win_list, players)

N, K = map(int, input().split())
relations = []

for i in range(N):
    relation = list(map(int, input().split()))
    relations.append(relation)
jihos = [i+1 for i in range(N)]
kyunghuis = list(map(int, input().split()))
minhos = list(map(int, input().split()))

for jiho in permutations(jihos, N):
    players = [jiho, kyunghuis, minhos]
    index = [0, 0, 0]
    win_list_list = [0, 0, 0]
    result = 0
    DFS(0, 1, index, win_list_list, players)
    if result:
        print(1)
        break
if not result:
    print(0)





