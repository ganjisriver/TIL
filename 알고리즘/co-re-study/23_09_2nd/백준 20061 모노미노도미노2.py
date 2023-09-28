from collections import deque

def drop_block(area_type, block_type, x, y):
    if area_type == "green":
        if block_type == 2:
            green_area[x].append(1)
            green_area[y].append(1)
        elif block_type == 3:
            green_area[]
        else:


    else:
        if block_type == 2:

        elif block_type == 3:

        else:


def check():


N = int(input())
green_area = [deque([0 for _ in range(6)]) for _ in range(4)]
blue_area = [deque([0 for _ in range(6)]) for _ in range(4)]
blue_max_line = []
green_max_line = 0
score = 0
for i in range(N):
    block = list(map(int, input().split()))
