TC = int(input())
for tc in range(1, TC+1):
    N, M = input().split()
    result = bin(int(M, 16))[2:]
    answer = '0'*(4*int(N) - len(result))+result
    print(f'#{tc} {answer}')