N = int(input())
N_list = list(map(int, input().split()))

min_value = min(N_list)
max_value = max(N_list)
print(f'{min_value} {max_value}')