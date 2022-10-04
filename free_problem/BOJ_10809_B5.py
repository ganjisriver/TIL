cnt_list = [-1]*123
S = input()
i = 0
for letter in S:
    if cnt_list[ord(letter)] == -1:
        cnt_list[ord(letter)] = i
    else:
        pass
    i += 1

for i in range(97, 123):
    print(cnt_list[i], end=' ')