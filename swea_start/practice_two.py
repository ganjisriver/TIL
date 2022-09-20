TC = int(input())
for tc in range(1, TC+1):
    N = input()
    temp = bin(int(N, 16))[2:]
    result = '0'*(4*len(N)-len(temp))+temp
    for i in range(0, len(result), 7):
        print(int(result[i:i+7], 2), end=' ')
    print()