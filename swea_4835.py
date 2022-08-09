TC = int(input())
for i in range(1, TC+1):
    N, M = map(int, input().split())
    num_list= list(map(int, input().split()))
    max_value = 0
    min_value = 10000001
    for j in range(N-M+1):
        result = 0
        for u in range(M):
            result += num_list[j+u]
        if result > max_value:
            max_value = result
        if result < min_value:
            min_value = result
            
    print(f'#{i} {max_value-min_value}')

