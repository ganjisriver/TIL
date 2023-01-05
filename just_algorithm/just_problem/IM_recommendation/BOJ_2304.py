N = int(input())
building_list = []
for i in range(N):
    idx, height = map(int, input().split())
    building_list.append((idx, height))
max_value = 0
max_value_idx = 0
answer = 0

for i in range(N):
    if max_value < building_list[i][1]:
        max_value = building_list[i][1]
        max_value_idx = building_list[i][0]

garage = [0]*1001
for i in range(N):
    garage[building_list[i][0]] = building_list[i][1]

current_value = 0
for j in range(0, max_value_idx+1):
    if not garage[j]:
        pass
    if garage[j] > current_value:
        current_value = garage[j]

    answer += current_value

current_value = 0
for k in range(1000, max_value_idx, -1):
    if not garage[k]:
        pass
    if garage[k] >= current_value:
        current_value = garage[k]
    answer += current_value

print(answer)

