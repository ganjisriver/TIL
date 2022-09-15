def inorder(n):
    if n > N:
        return
    if (n*2) <= N:
        inorder(n*2)
    ans_list.append(ch1[n])
    if (n*2+1) <= N:
        inorder(n*2+1)


for tc in range(1, 11):
    N = int(input())
    ch1 = [0]*(N+1)
    for i in range(N):
        arr = list(input().split())
        ch1[int(arr[0])] = arr[1]
    ans_list = []
    inorder(1)
    ans = ''.join(ans_list)
    print(f'#{tc} {ans}')