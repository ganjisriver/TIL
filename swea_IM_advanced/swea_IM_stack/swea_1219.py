for tc in range(1, 11):
    T, E = map(int, input().split())
    matrix = [[0]*100 for _ in range(100)]
    idx_list = list(map(int, input().split()))
    for i in range(E):
        start = idx_list[i*2]
        end = idx_list[i*2+1]
        matrix[start][end] = 1

    stack = [0]
    visited = []

    while stack:
        current = stack.pop()
        visited.append(current)

        for destination in range(100):
            if matrix[current][destination]:
                stack.append(destination)
        if 99 in visited:
            print(f'#{tc} 1')
            break

    if 99 not in visited:
        print(f'#{tc} 0')

