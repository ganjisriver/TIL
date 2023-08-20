# dfs
from collections import deque

N, M = map(int, input().split())

task_dict = dict()
for i in range(M):
    pre, nxt = map(int, input().split())
    if nxt not in task_dict:
        task_dict[nxt] = [pre]
    else:
        task_dict[nxt].append(pre)
target = int(input())

dfs_stack = [target]
answer = 0
visited = set()
visited.add(target)
while dfs_stack:
    current = dfs_stack.pop()
    if current in task_dict:
        for i in task_dict[current]:
            if i not in visited:
                answer += 1
                dfs_stack.append(i)
                visited.add(i)

print(answer)
