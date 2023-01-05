S = '666'
N = int(input())
cnt = 0
s = 666
while cnt != N:
    s = str(s)
    for i in range(len(s)-2):
        if s[i] == '6' and s[i+1] == '6' and s[i+2] == '6':
            cnt += 1
            break
    s = int(s)
    s += 1

print(s-1)