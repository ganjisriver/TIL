TC = int(input())
for tc in range(1, TC+1):
    matrix = [list(input()) for _ in range(5)]
    max_value = 0
    stack = []
    for i in range(5):
        if max_value < len(matrix[i]):
            max_value = len(matrix[i])
    for i in range(5):
        while len(matrix[i]) < max_value:
            if len(matrix[i]) < max_value:
                matrix[i].append('_')

    for i in range(max_value):
        for j in range(5):
            if matrix[j][i] == '_':
                pass
            else:
                stack.append(matrix[j][i])
    s = ''.join(stack)
    print(f'#{tc} {s} ')




