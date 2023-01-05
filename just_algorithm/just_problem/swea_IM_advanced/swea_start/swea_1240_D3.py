pattern = {0: '0001101',
           1: '0011001',
           2: '0010011',
           3: '0111101',
           4: '0100011',
           5: '0110001',
           6: '0101111',
           7: '0111011',
           8: '0110111',
           9: '0001011'}

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    flag = True
    odd_code = 0
    even_code = 0
    temp = str()
    for t in range(0, N-5):
        for i in range(M-1, M-57, -1):
            if arr[t][i] == '1':
                temp = arr[t][i-55:i+1]
                print(arr[t][i-55:i+1])
                flag = False
                break
        if not flag:
            break

    for i in range(0, 56, 7):
        for j in range(10):
            if temp[i:i+7] == pattern.get(j):
                if i % 2 == 0:
                    odd_code += j
                else:
                    even_code += j
    result = odd_code*3 + even_code
    if result % 10 == 0:
        print(f'#{tc} {odd_code + even_code}')
    else:
        print(f'#{tc} 0')



