a = int(input())
sum=0
for i in range(4):
    if a<=0:
        break;
    j = a%10
    a = int(a/10)
    sum=sum+j
print(sum)