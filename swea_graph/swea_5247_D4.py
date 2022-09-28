from collections import deque
T = int(input())
for tc in range(1, T+1):
    answer = 0
    N, M = map(int, input().split())
    visited = set()
    q = deque()
    q.append((N,0))
    while q:
        (value, cnt) = q.popleft()
        if value in visited:
            continue
        visited.add(value)

        if value == M:
            answer = cnt
            break

        if value*2 <= 1000000 and value*2 not in visited:
            q.append((value*2, cnt + 1))

        if value + 1 not in visited:
            q.append((value+1, cnt+1))

        if value - 1 not in visited:
            q.append((value-1, cnt+1))

        if value - 10 not in visited:
            q.append((value-10, cnt+1))

    print(f'#{tc} {answer}')