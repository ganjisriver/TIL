arr = ['A', 'B', 'C', 'D']
sel = [0,0]

def perm_rep(depth):
    if depth == 2:
        print(*sel)
        return

    for i in range(4):
        sel[depth] = arr[i]
        perm_rep(depth+1)

perm_rep(0)