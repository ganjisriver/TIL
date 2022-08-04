a = int(input())
b = list(map(int, input().split()))
b.sort()
index = (n-1)//2
print("{}".format(b[index]))
    