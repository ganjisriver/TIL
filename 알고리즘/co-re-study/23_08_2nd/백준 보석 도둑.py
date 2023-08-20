## 1차시도 시간초과
# N, K = map(int, input().split())
#
# jewel_list = []
# for i in range(N):
#     mass, value = map(int, input().split())
#     value_per_mass = value // mass
#     jewel_list.append((value_per_mass, mass, value))
#
# answer = 0
# bag_list = []
# for i in range(K):
#     bag = int(input())
#     bag_list.append(bag)
# jewel_list.sort(reverse=True)
# bag_list.sort()
# visited = set()
#
# for i in range(N):
#     for j in range(K):
#         if j in visited:
#             continue
#         if jewel_list[i][1] < bag_list[j]:
#             visited.add(j)
#             answer += jewel_list[i][2]
#             break
# print(answer)

N, K = map(int, input().split())

jewel_list = []
for i in range(N):
    mass, value = map(int, input().split())
    value_per_mass = value // mass
    jewel_list.append((value_per_mass, mass, value))

answer = 0
bag_list = []
for i in range(K):
    bag = int(input())
    bag_list.append(bag)
jewel_list.sort(reverse=True)
bag_list.sort()
visited = set()

for i in range(N):
    for j in range(K):
        if j in visited:
            continue
        if jewel_list[i][1] < bag_list[j]:
            visited.add(j)
            answer += jewel_list[i][2]
            break
print(answer)