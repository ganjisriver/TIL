from collections import deque
import sys
input=sys.stdin.readline
q = deque()
N = int(input())
for i in range(N):
    command = input().split()
    if command[0] == "push":
        q.append(command[1])

    elif command[0] == "pop":
        if q:
            print(q.popleft())
        else:
            print(-1)

    elif command[0] == "size":
        print(len(q))

    elif command[0] == "empty":
        if q:
            print(0)
        else:
            print(1)

    elif command[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)

    elif command[0] == "back":
        if q:
            print(q[-1])
        else:
            print(-1)
