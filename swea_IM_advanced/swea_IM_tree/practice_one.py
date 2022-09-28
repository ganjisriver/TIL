def preorder(n):
    if n:
        print(n, end=' ')
        preorder(ch1[n])
        preorder(ch2[n])

V = int(input())
arr = list(map(int, input().split()))
root = 1
E = V - 1
ch1 = [0]*(V+1)
ch2 = [0]*(V+1)

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c

preorder(root)