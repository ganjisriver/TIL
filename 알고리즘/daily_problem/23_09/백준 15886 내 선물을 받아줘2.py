N = int(input())
roads = input()

cnt = 0
for i in range(N-1):
    if roads[i:i+2] == "EW":
        cnt += 1
print(cnt)
