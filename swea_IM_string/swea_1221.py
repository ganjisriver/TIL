import sys
sys.stdin = open('GNS_test_input.txt')
TC = int(input())
for tc in range(1, TC+1):
    N, K = input().split()
    String_list = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    idx_list = [0]*10
    sorted_list = []
    value_list = list(input().split())

    for i in range(int(K)):
        for j in range(10):
            if value_list[i] == String_list[j]:
                idx_list[j] += 1

    print(f'#{tc}')
    for i in range(10):
        for j in range(idx_list[i]):
            print(f'{String_list[i]}', end=' ')
    print()





