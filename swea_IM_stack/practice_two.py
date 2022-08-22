<<<<<<< HEAD
V, E = map(int, input().split())

adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]

for _ in range(E):
    start, end = map(int, input().split())
    adj_matrix[start][end] = 1
    adj_matrix[end][start] = 1

stack = [1]
visited = []

while stack:
    current = stack.pop()
    if current not in visited:
        visited.append(current)

    for destination in range(V+1):
        if adj_matrix[current][destination] and destination not in visited:
            stack.append(destination)

print('이동경로:', *visited)
=======
TC = int(input())
for tc in range(1, TC+1):
    garo = input()
    stack = []
    for i in garo:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not stack:
                stack.append(i)
                break

            elif i == ')' and stack[-1] != '(':
                stack.append(i)
                break

            else:
                stack.pop()

    if stack:
        print("#{} -1".format(tc))

    else:
        print("#{} 1".format(tc))
>>>>>>> 7a996084a1a27ad6d1c9f62d1d7ad998111e3fc6
