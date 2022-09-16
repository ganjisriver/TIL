def calculator(i):
    if tree[i] not in cal:
        return
    elif tree[i] in cal:        
        calculator(int(arr[i - 1][2]))        
        calculator(int(arr[i - 1][3]))
        if tree[int(arr[i - 1][2])] not in cal and tree[int(arr[i - 1][3])] not in cal:
            if tree[i] == '*':
                tree[i] = int(tree[int(arr[i - 1][2])])*int(tree[int(arr[i - 1][3])])
            elif tree[i] == '/':
                tree[i] = int(tree[int(arr[i - 1][2])])/int(tree[int(arr[i - 1][3])])
            elif tree[i] == '+':
                tree[i] = int(tree[int(arr[i - 1][2])]) + int(tree[int(arr[i - 1][3])])
            elif tree[i] == '-':
                tree[i] = int(tree[int(arr[i - 1][2])])-int(tree[int(arr[i - 1][3])])

cal = ['*', '/', '+', '-']
for tc in range(1, 11):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    tree = [0]
    for i in range(len(arr)):
        tree.append(arr[i][1])
    calculator(1)
    print(f'#{tc} {int(tree[1])}')

