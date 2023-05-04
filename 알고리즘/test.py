from itertools import combinations
def solution(n, edges):
    answer = 0
    tmp = [i+1 for i in range(n)]
    three_nodes = list(combinations(tmp, 3))
    nodes_value = [[0]*3]*len(three_nodes)
    trees = [[] for _ in range(n+1)]

    for i in range(len(edges)):
        trees[edges[i][0]].append(edges[i][1])
        trees[edges[i][1]].append(edges[i][0])

    while

    for i in range(len(three_nodes)):
        three_nodes[i]
        visited = set()
        queue = []
        while queue:






    return three_nodes
n1 = 4
edges1 = [[1,2],[2,3],[3,4]]
n2 = 5
edges2 = [[1,5],[2,5],[3,5],[4,5]]

print(solution(n1, edges1))
print(solution(n2, edges2))