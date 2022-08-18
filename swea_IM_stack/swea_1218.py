for tc in range(1, 11):
    length = int(input())
    garo = input()
    stack = []
    for i in garo:
        if i == '(' or i == '{' or i =='[' or i == '<':
            stack.append(i)
        elif i == ')' or i == '}' or i == ']' or i == '>':
            if not stack:
                stack.append(i)
                break

            elif (i == ')' and stack[-1] != '(') or (i == '}' and stack[-1] != '{') or (i == ']' and stack[-1] != '[') or (i == '>' and stack[-1] != '<'):
                stack.append(i)
                break

            elif  (i == ')' and stack[-1] == '(') or (i == '}' and stack[-1] == '{') or (i == ']' and stack[-1] == '[') or (i == '>' and stack[-1] == '<'):
                stack.pop()
            else:
                pass


    if stack:
        print("#{} 0".format(tc))

    else:
        print("#{} 1".format(tc))
