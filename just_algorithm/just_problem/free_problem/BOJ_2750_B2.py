T = int(input())
num_list = []
for i in range(1, T+1):
    N = int(input())
    num_list.append(N)
num_list.sort()
for i in range(len(num_list)):
    print(num_list[i])