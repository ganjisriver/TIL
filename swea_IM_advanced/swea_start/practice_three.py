pattern = {0: '001101',
           1: '010011',
           2: '111011',
           3: '110001',
           4: '100011',
           5: '110111',
           6: '001011',
           7: '111101',
           8: '011001',
           9: '101111'}

TC = int(input())
for tc in range(1, TC+1):
    N = input()
    temp = bin(int(N, 16))[2:]
    index = '0'*(4*len(N) - len(temp))+ temp
    result = index[len(N)//2:-len(N)//2]
    for i in range(0, len(index)-6, 6):
        for j in range(10):
            if result[i:i+6] == pattern.get(j):
                print(result[i:i+6])


