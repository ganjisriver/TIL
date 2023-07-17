def solution(s, N):
    answer = -1
    number_set = set()
    for i in range(1, N+1):
        number_set.add(i)
    for idx in range(len(s) - N):
        visited_set = set()
        candidate_substring = ""
        for j in range(idx, idx+N):
            current_number = int(s[j])
            if current_number in number_set and current_number not in visited_set:
                candidate_substring += s[j]
                visited_set.add(current_number)
            else:
                break
        if len(candidate_substring) == N and int(candidate_substring) > answer:
            answer = int(candidate_substring)


    return answer

print(solution("1451232125", 2))
print(solution("313253123", 3))
print(solution("12412415", 4))