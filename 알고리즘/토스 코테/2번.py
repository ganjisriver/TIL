from collections import deque
def solution(relationships, target, limit):
    answer = 0
    friend_relation_tree = dict()
    for one, two in relationships:
        if one in friend_relation_tree:
            friend_relation_tree[one].append(two)
        else:
            friend_relation_tree[one] = [two]
        if two in friend_relation_tree:
            friend_relation_tree[two].append(one)
        else:
            friend_relation_tree[two] = [one]
    visited = set()
    visited.add(target)
    friend_queue = deque([(target, 0)])
    while friend_queue:
        current, step = friend_queue.popleft()
        if step >= limit:
            break
        for current_friend in friend_relation_tree[current]:
            if current_friend not in visited:
                visited.add(current_friend)
                friend_queue.append((current_friend, step+1))
                if step == 0:
                    answer += 5
                elif step > 0:
                    answer += 11
    return answer

# def find(current_person, friend_root):
#     if friend_root[current_person] != current_person:
#         friend_root[current_person] = find(friend_root[current_person])
#     return friend_root[current_person]
# def union(friend_one, friend_two):
#     friend_one_root = find(friend_one)
#     friend_two_root = find(friend_two)


print(solution([[1,2], [2,3], [2,6], [3,4], [4,5]], 2, 3))
print(solution([[1,2],[2,3], [2,6], [3,4], [4,5]], 1, 2))