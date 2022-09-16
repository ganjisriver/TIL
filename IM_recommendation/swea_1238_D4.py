for tc in range(1, 11):
    N, S = map(int, input().split())
    idx = list(map(int, input().split()))
    arr = [[0]*101 for _ in range(101)]
    for i in range(N//2):
        start, end = idx[2*i], idx[2*i+1]
        arr[start][end] = 1
    stack = [S]
    visited = []
    before_visited = []
    flag = True
    while flag:
        for _ in range(len(stack)):
            current = stack.pop(0)
            if current not in visited:
                visited.append(current)
            for destination in range(101):
                if arr[current][destination] and destination not in visited:
                    stack.append(destination)

        if len(visited) == len(before_visited):
            break
        else:
            cnt = len(visited) - len(before_visited)
            for i in range(1, cnt+1):
                before_visited.append(visited[-i])
    last_list = []
    for i in range(1, cnt+1):
        last_list.append(visited[-i])
    result = max(last_list)
    print(f'#{tc} {result}')

