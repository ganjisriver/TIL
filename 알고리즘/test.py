import sys
from collections import deque
input=sys.stdin.readline
N = int(input())
for i in range(N):
    kwalho_strings = input()
    kwalho_queue = deque()
    flag = True
    for j in range(len(kwalho_strings)):
        if kwalho_strings[j] == "(":
            kwalho_queue.append(kwalho_strings[j])
        elif kwalho_strings[j] == ")":
            if not kwalho_queue:
                flag = False
                break
            else:
                kwalho_queue.popleft()
    if flag and not kwalho_queue:
        print("YES")
    else:
        print("NO")
