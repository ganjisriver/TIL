import sys
input=sys.stdin.readline
N, K = map(int, input().split())
default_N = str(N)
flag = True
answer = 1
cnt = 1
if K == 1 or N % K == 0:
    flag = False
else:
    mok = 10000 // K
    while cnt < mok:
        if N % K == 0:
            flag = False
            break
        else:
            N = str(N)
            N = N + default_N
            N = int(N)
            cnt += 1
if flag:
    print("-1")
else:
    print(cnt)

# import sys
# input=sys.stdin.readline
# N, K = map(int, input().split())
# default_N = str(N)
# flag = True
# cnt = 1
# if N % K == 0:
#     flag = False
#     cnt = 1
# elif K % 10 == 0:
#     flag = False
#     cnt = -1
# else:
#     cnt = K
# print(cnt)