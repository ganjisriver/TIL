# def preorder(idx):
#     predorder


V, E = map(int, input().split())
E_list = list(map(int, input().split()))

for i in range(E//2):
    parent, child = E_list[2*i], E_list[2*i+1]
    left = [0]*(V+1)
    right = [0]*(V+1)


