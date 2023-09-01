import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline
N, M = map(int, input().split())
arr_list = sorted(list(map(int, input().split())))
for arr in sorted(list(set(combinations_with_replacement(arr_list, M)))):
    print(*arr)