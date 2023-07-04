import sys
input=sys.stdin.readline
N, K = map(int, input().split())
default_N = str(N)
flag = True
cnt = 1
while flag:
    if N % K == 0:
        flag = False
    else:
        N = str(N)
        N = N+default_N
        N = int(N)
        cnt += 1
    if cnt > 10000:
        flag = False
        cnt = -1
print(cnt)