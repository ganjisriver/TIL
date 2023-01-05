N = int(input())
word_list = []

for _ in range(N):
    s = input()
    word_list.append(s)

word_list = list(set(word_list))
word_list.sort(key=lambda x : (len(x), x))

print("\n".join(word_list))