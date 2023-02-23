def solution(info, query):
    answer = [0 for _ in range(len(query))]

    info.sort(key=lambda x: int(x.split()[4])) # 인포를 점수순으로 정렬

    # 쿼리를 돌려서 인포랑 비교할거임
    for i in range(len(query)):
        require_lan, require_position, require_career, require_food = query[i].split()[0], query[i].split()[2], query[i].split()[4], query[i].split()[6]
        require_score = int(query[i].split()[7]) # 쿼리에서의 기준 점수를 정해서 그 아래는 다 탈락
        start, end = 0, len(info)-1

        # 점수를 기준으로 이진 탐색을 통해 어느정도 거름
        while start <= end:
            mid = (start + end) // 2
            target = int(info[mid].split()[4])
            if  target < require_score:
                start = mid + 1
            else:
                end = mid - 1

        adjusted_info = info[mid:][:]
        if mid == len(info)-1:
            adjusted_info = [info[-1]]


        for j in range(len(adjusted_info)):
            info_lan, info_position, info_career, info_food = adjusted_info[j].split()[0], adjusted_info[j].split()[1], adjusted_info[j].split()[2], adjusted_info[j].split()[3]
            if require_lan == info_lan or require_lan == '-':
                pass
            else:
                continue
            if require_position == info_position or require_position == '-':
                pass
            else:
                continue
            if require_career == info_career or require_career == '-':
                pass
            else:
                continue
            if require_food == info_food or require_food == '-':
                pass
            else:
                continue
            answer[i] += 1

    return answer

inf= ["java backend junior pizza 100",
      "python frontend senior chicken 100",
      "python frontend senior chicken 100",
      "cpp backend senior pizza 260",
      "java backend junior chicken 100",
      "python backend senior chicken 100"]

q = ["java and backend and junior and pizza 100",
     "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250",
     "- and backend and senior and - 150",
     "- and - and - and chicken 100",
     "- and - and - and - 150"]

print(solution(inf, q))

# 람다 함수를 위해 참고 블로그
# https://gorokke.tistory.com/38