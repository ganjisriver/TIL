N, M, K = map(int, input().split())
candis_num = [0]+list(map(int, input().split()))
root = [0]*(N+1)
zip_dan = []

for i in range(M):
    friend1, friend2 = map(int, input().split())
