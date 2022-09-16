from itertools import combinations

TC = int(input())
for tc in range(1, TC+1):
    N, B = map(int, input().split())
    clerk = list(map(int, input().split()))
    clerk_tall = set()
    result = 1000001
    for i in range(1, len(clerk)+1):
        for j in list((combinations(clerk, i))):
            clerk_tall.add(sum(j))
            if sum(j) == B:
                result = B
                break
        if result == B:
            break

    if result != B:
        for i in clerk_tall:
            if B < i < result:
                result = i

    print(f'#{tc} {result - B}')
