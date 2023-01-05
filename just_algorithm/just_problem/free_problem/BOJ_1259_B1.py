while True:
    flag = True
    N = input()
    string_list = []

    if N == '0':
        break
    for i in range(len(N)):
        string_list.append(N[i])
    reversed_list = list(reversed(string_list))
    if reversed_list[0] == '0':
        flag = False

    if string_list != reversed_list:
        flag = False
    if flag:
        print('yes')
    else:
        print('no')