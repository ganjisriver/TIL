def soultion(survey, choices):
    #유형 검사 유형 순서대로 key값으로 추가 value 초기값은 0
    type_dict = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    answer = ''

    # survey길이만큼 반복문을 통해 딕셔너리 내부 값 변경
    for i in range(len(survey))
        #생각해보니 두가지 유형 중 한개씩만 조정해서 결과내도 상관없음
        first_thing = survey[i][:1]

        # 딕셔너리에 choice 결과 반영
        value = 4 - choices[i]
        type_dict[first_thing] = type_dict[first_thing] + value

    #반복문 돌기 위한 키값으로 이루어진 리스트 생성
    dict_key = list(type_dict.keys())

    # 성격유형 검사 위해 대조군끼리 비교하는 for문 돌리기 결과를 answer에 하나씩 추가
    for j in range(4):
        # 어차피 앞에 값이 ABC순으로 더 빠르기 때문에 초과가 아니라 이상으로 적용
        if type_dict[dict_key[j*2]] >= type_dict[dict_key[j*2+1]]:
            answer += dict_key[j*2]
        else:
            answer += dict_key[j*2+1]
    return answer

