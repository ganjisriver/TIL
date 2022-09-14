X = int(input())
N = int(input())
result = 0
for _ in range(N):
    x, y = map(int, input().split())
    result += x*y

if result == X:
    print('Yes')

else:
    print('No')