def solution(today, terms, privacies):
    answer = []

    today_year, today_month, today_day = today.split('.')
    int_today = int(today_year + today_month + today_day)
    terms_dict = {}

    for i in range(len(terms)):
        term_type, term_period = terms[i].split()
        terms_dict[term_type] = term_period

    for k in range(len(privacies)):
        privacy, privacy_type = privacies[k].split()
        privacy_year, privacy_month, privacy_day = privacy.split('.')
        term_type_month = terms_dict.get(privacy_type)
        privacy_year = int(privacy_year)
        privacy_month = int(privacy_month) + int(term_type_month)

        while privacy_month > 12:
            privacy_year += 1
            privacy_month -= 12
        privacy_year = str(privacy_year)
        privacy_month = str(privacy_month)

        if len(privacy_month) == 1:
            privacy_month = '0' + privacy_month

        privacy = privacy_year + privacy_month + privacy_day
        if int_today >= int(privacy):
            answer.append(k + 1)
    return answer

today = '2022.08.12'
terms = ["A 24", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

print(solution(today, terms, privacies))