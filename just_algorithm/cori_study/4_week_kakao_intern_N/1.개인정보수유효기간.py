def solution(today, terms, privacies):
    answer = []
    today = ''.join(today.split('.'))
    terms_dict = dict()
    for term in terms:
        key, value = term.split(' ')
        terms_dict[key] = value
    for i in range(len(privacies)):
        privacy_term, term = privacies[i].split(' ')
        privacy_date = ''.join(privacy_term.split('.'))
        privacy_month = int(privacy_date[4:6]) + int(terms_dict[term])
        if  privacy_month & 12 >= 1:
            if 1 < privacy_month & 12
            privacy_date = str(int(privacy_date[0:4])+1) + '0'*(privacy_month & 12) + str(privacy_month - (privacy_month - 12)) + privacy_date[6:]
        else:
            privacy_date = privacy_date[0:4] + str(privacy_month) + privacy_date[6:]
        if int(today) - int(privacy_date) > 0:
            answer.append(i+1)
    return answer

today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

print(solution(today, terms, privacies))