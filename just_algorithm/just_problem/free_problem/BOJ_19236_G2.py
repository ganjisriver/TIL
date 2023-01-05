direction = {
    1: (-1, 0), 2: (-1, -1), 3: (0, -1), 4: (1, -1), 5: (1, 0), 6: (1, 1), 7: (0, 1), 8: (-1, 1)}
def moving_fish(fish_idx, subset_fish_life):
    for i in range(len(subset_fish_life)):




def moving_shark(shark_idx ,chance, subset_fish_life):


fish_area = [[]*4 for _ in range(4)]
fish_life = []
fish_life.sort()
shark = 999
cnt = 0

for i in range(4):
    fish_list = list(map(int, input().split()))
    for j in range(4):
        fish_area[i].append((fish_list[2*j], fish_list[2*j+1]))
        fish_life.append((fish_list[2*j], fish_list[2*j+1]))

fish_area[0][0] = (shark, fish_area[0][0][1])
moving_shark(fish_area[0][0], 0, fish_life)
print(fish_area[0][0])
