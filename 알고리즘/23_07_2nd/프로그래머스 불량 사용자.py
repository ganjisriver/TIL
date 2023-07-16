from itertools import combinations, permutations
def is_banned(combi_users, banned_id):
    for i in range(len(banned_id)):
        if len(combi_users[i]) != len(banned_id[i]):
            return False

        for j in range(len(combi_users[i])):
            if banned_id[i][j] == "*" or (banned_id[i][j] == combi_users[i][j]):
                pass
            else:
                return False
    return True

def solution(user_id, banned_id):
    combi_list = list(combinations(user_id, len(banned_id)))
    ban_list = set()
    cnt = 0
    for combi_users in combi_list:
        if not is_banned(combi_users, banned_id):
            pass
        else:
            cnt += 1
            combi_user_set = set(combi_users)
            if combi_user_set not in ban_list:
                ban_list.add(combi_users)
    answer = len(ban_list)
    return answer

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))