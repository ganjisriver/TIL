powerset_idx = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(1<<10):
    stack = []
    result = 0
    for j in range(10):
        if i & (1<<j):
            stack.append(powerset_idx[j])
    for k in stack:
        result += k
    if result == 10:
        print(*stack)

