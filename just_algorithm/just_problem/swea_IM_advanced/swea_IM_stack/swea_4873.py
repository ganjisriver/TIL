TC = int(input())
for tc in range(1, TC+1):
    s = input()
    stack = []
    for i in s:
        if stack and i == stack[-1]:
            stack.pop()

        elif not stack or i != stack[-1]:
            stack.append(i)

    print(f'#{tc} {len(stack)}')