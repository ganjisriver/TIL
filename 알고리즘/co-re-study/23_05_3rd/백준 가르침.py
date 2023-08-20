from itertools import combinations
N, K = map(int, input().split())
default_word_set = set()
default_word_set.add('a')
default_word_set.add('n')
default_word_set.add('t')
default_word_set.add('i')
default_word_set.add('c')
answer = 0
idx_dict = dict()
new_char_set = set()
can_learn_char_cnt = K-5
check_impossible = set()
for i in range(N):
    if K < 5:
        new_word = input()
        continue
    else:
        new_word = input()
        if len(new_word) == can_learn_char_cnt:
            answer += 1
            continue
        for j in range(4, len(new_word)-3):
            if i not in idx_dict:
                idx_dict[i] = set()
            if new_word[j] not in default_word_set:
                new_char_set.add(new_word[j])
                idx_dict[i].add(new_word[j])
            if len(idx_dict[i]) > can_learn_char_cnt:
                check_impossible.add(i)
                break
                # TODO: 여기서 check_possible을 set으로 두고 넣는 방식으로 가야할듯
                # TODO: 아래 for문에서 돌려야됨 조합을
new_char_list = list(new_char_set)
if not new_char_list:
    print(answer)
else:
    arr = list(combinations(new_char_list, can_learn_char_cnt))
    for i in range(N):
        if check_impossible[i]:
            continue
        for j in range(len(idx_dict[i])):
            tmp = idx_dict[i]







