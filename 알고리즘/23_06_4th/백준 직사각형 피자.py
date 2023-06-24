import sys
input = sys.stdin.readline
W, H, K = map(int, input().split())
N = int(input())
height_cutting_idx_list = [0] + list(map(int, input().split())) + [H]
M = int(input())
width_cutting_idx_list = [0] + list(map(int, input().split())) + [W]

width_length_list = []
height_length_list = []
for i in range(N+1):
    width_length = width_cutting_idx_list[i+1] - width_cutting_idx_list[i]
    width_length_list.append(width_length)
for j in range(M+1):
    height_length = height_cutting_idx_list[j+1] - height_cutting_idx_list[j]
    height_length_list.append(height_length)
width_length_list.sort()
height_length_list.sort()
answer = 0


