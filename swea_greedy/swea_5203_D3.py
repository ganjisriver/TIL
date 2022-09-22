T = int(input())
for tc in range(1, T+1):
    card_list = list(map(int, input().split()))
    player_one = [0]*10
    player_two = [0]*10
    cnt = 0
    answer = 0
    player_one_win = False
    player_two_win = False
    for i in range(12):
        if i % 2 == 0:
            player_one[card_list[i]] += 1
        if i % 2 == 1:
            player_two[card_list[i]] += 1
        cnt += 1
        if cnt >= 5:
            for j in range(10):
                if player_one[j] == 3:
                    player_one_win = True
                if player_two[j] == 3:
                    player_two_win = True
            for k in range(8):
                if player_one[k] and player_one[k+1] and player_one[k+2]:
                    player_one_win = True
                if player_two[k] and player_two[k+1] and player_two[k+2]:
                    player_two_win = True
        if player_one_win or player_two_win:
            break

    if not player_one_win and not player_two_win:
        print(f'#{tc} 0')
    elif player_one_win and not player_two_win:
        print(f'#{tc} 1')
    elif player_two_win and not player_one_win:
        print(f'#{tc} 2')






