# 최초 답안
def solution(k, room_number):
    for room in room_number:
        findroom(room)
    return answer

def findroom(room):
    if room not in visited:
        visited.add(room)
        answer.append(room)
    else:
        findroom(room + 1)
answer = []
visited = set()
print(solution(10, [1,3,4,1,3,1]))

# 2차 수정


