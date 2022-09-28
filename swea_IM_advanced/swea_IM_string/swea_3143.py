TC = int(input())
for tc in range(1, TC+1):
    A, B = input().split()
    cnt = 0
    for i in range(len(A)-len(B)):
        if A[i:i+len(B)] == B:
            cnt += len(B)-1
    result = len(A) - cnt
    print(f'#{tc} {result}')

