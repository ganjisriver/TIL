import heapq
from heapq import heapify
N, C = map(int, input().split())
house_idx_list = []
min_idx = 10000000000000
max_idx = 0
for i in range(N):
    home_idx = int(input())
    house_idx_list.append(home_idx)
    if home_idx > min_idx:
        min_idx = home_idx
    if home_idx < max_idx:
        max_idx = home_idx

house_idx_list.sort()
while min_idx <= max_idx:
    pass

