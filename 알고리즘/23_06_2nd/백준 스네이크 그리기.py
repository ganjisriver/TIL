import sys

# 원리는 알았는데 구현하기 귀찮
n, m = map(int, input().split())

if (n % 2) == 1 and (m % 2) == 1:
    print(n * m - 1)
    default_set = set()
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 2 and j == 2:
                continue
            print(i, j)

else:
    print(n*m)
    for i in range(1, n+1):
        for j in range(1, m+1):
            print(i, j)

