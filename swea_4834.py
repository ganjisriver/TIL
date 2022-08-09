TC = int(input())
for i in (1, TC+1):
    value_len = int(input())
    value = list(map(int, input()))
    max_cnt = 0
    max_value = 0
    cnt = [0]*10
    for k in value:
        cnt[k] += 1
    
    for j in range(10):
        if cnt[j] == 0:
            continue
        else:
            if cnt[j] >= max_cnt:
               max_cnt = cnt[j]
               max_value = j
    
    print(f'#{i} {max_value} {max_cnt}')