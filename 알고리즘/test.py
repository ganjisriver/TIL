from collections import deque
import sys
queue = deque()
input=sys.stdin.readline
N = int(input())
for i in range(N):
    command = input().split()
    if len(command) == 1:
        command = command[0]
        if command == "pop_front":
            if queue:
                print(queue.popleft())
            else:
                print('-1')
        elif command == "pop_back":
            if queue:
                print(queue.pop())
            else:
                print('-1')
        elif command == "size":
            print(len(queue))
        elif command == "empty":
            if queue:
                print("0")
            else:
                print("1")
        elif command == "front":
            if queue:
                print(queue[0])
            else:
                print("-1")
        elif command == "back":
            if queue:
                print(queue[-1])
            else:
                print("-1")
    else:
        
