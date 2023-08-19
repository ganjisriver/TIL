def gcb(a, b):
    if b > a:
        a, b = b, a
    while b > 0:
        a, b = b, (a % b)
    return a

N = int(input())
num_list = list(map(int, input().split()))
X = int(input())
answer = 0
cnt = 0
for num in num_list:
    result = gcb(X, num)
    if result == 1:
        answer += num
        cnt += 1
print(answer/cnt)