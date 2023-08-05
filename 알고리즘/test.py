N = int(input())
arr = []
answer = [1]*N
for i in range(N):
    weight, height = map(int, input().split())
    arr.append((weight, height, i))
arr.sort()
for i in range(N-1):
    for j in range(i, N):
        if arr[i][1] < arr[j][1] and arr[i][0] < arr[j][0]:
            answer[arr[i][2]] += 1
print(*answer)