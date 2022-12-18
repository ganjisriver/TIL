N = int(input())
num_list = list(map(int, input().split()))
v = int(input())
cnt = 0
for i in range(len(num_list)):
    if num_list[i] == v:
        cnt +=1
print(cnt)