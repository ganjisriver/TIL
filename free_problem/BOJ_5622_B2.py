phone = [0, 0, 'ABC', 'DEF','GHI','JKL','MNO','PQRS','TUV', 'WXYZ']

S = input()
cnt = 0
for i in range(2, 10):
    for j in range(len(phone[i])):
        for k in range(len(S)):
            if S[k] in phone[i][j]:
                cnt += i+1
print(cnt)