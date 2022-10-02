N = list(map(int, input().split()))
ans = []
ascending = [1, 2, 3, 4, 5, 6, 7, 8]
descending = [8, 7, 6, 5, 4, 3, 2, 1]
for i in range(len(N)):
    ans.append(N[i])

if ans == ascending:
    print('ascending')

elif ans == descending:
    print('descending')

else:
    print('mixed')