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