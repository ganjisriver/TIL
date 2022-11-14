num_list = []
average = 0
for i in range(5):
    N = int(input())
    average += N
    num_list.append(N)
num_list.sort()
print(average//5)
print(num_list[2])