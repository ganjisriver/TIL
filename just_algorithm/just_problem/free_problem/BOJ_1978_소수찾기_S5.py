N = int(input())
numbers = list(map(int, input().split()))

sosu = 0
for num in numbers:
    if num == 1:
        continue
    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break
    if flag == True:
        sosu += 1
print(sosu)