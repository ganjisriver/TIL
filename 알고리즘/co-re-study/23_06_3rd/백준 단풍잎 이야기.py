from itertools import combinations
import sys
input=sys.stdin.readline

n, m, k = map(int, input().split())

arr = [i+1 for i in range(2*n)]
combi_list = list((combinations(arr, n)))

skills = [list(map(int, input().split())) for _ in range(m)]

for i in range(len(combi_list)):
    combi_list[i] = set(combi_list[i])

answer = 0
for i in range(len(combi_list)):
    cnt = 0
    for j in range(len(skills)):
        flag = True
        for t in range(k):
            if skills[j][t] not in combi_list[i]:
                flag = False
                break
        if flag:
            cnt += 1
    if cnt > answer:
        answer = cnt
print(answer)