TC = int(input())
for tc in range(1, TC+1):
    A = input()
    B = input()
    result = 0
    for i in range(len(B)-len(A)+1):
        if B[i:i+len(A)] == A:
            result = 1

    print(f'#{tc} {result}')