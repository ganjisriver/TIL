# import sys
# from collections import deque
#
# N, M = map(int, sys.stdin.readline().split())
#
# relation = [[] for _ in range(N+1)]
# for i in range(M):
#     x, y = map(int, sys.stdin.readline().split())
#     relation[x].append(y)
#     relation[y].append(x)
#
# visited = set()
# odd_check = set()
# even_check = set()
# queue = deque()
# queue.append(x)
# odd_check.add(x)
# flag = False
# while queue:
#     current = queue.popleft()
#     visited.add(current)
#     for i in relation[current]:
#         if i not in visited:
#             if current in odd_check:
#                 even_check.add(i)
#             else:
#                 odd_check.add(i)
#             queue.append(i)
#         elif i in visited:
#             if current in odd_check and (i in odd_check):
#                 flag = True
#                 break
#             elif current in even_check and (i in even_check):
#                 flag = True
#                 break
#     if flag:
#         break
#
# if flag:
#     print(0)
#
# if not flag:
#     print(1)


