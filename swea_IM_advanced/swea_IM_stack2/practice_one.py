TC = int(input())
for tc in range(1, TC+1):
    N = input()
    stack = []
    print(f'{tc}', end=' ')
    for i in N:
        if i == '+' or i == '/' or i == '-' or i =='*':
            stack.append(i)
        else:
            print(i, end='')
    while stack:
        operator = stack.pop()
        print(operator, end='')
    print()