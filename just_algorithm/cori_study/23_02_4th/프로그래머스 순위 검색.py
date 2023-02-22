def solution(info, query):
    answer = []
    info_index = [0 for _ in range(len(query))]
    for i in range(len(query)):

        for j in range(len(info)):
            query[i]

    return answer

inf= ["java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"]

q = ["java and backend and junior and pizza 100",
         "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250",
         "- and backend and senior and - 150",
         "- and - and - and chicken 100",
         "- and - and - and - 150"]

print(solution(inf, q))