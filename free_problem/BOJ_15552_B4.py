import sys

N = int(input())
for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)