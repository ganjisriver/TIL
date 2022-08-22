for tc in range(1, 11):
    matrix = [input() for _ in range(100)]

    # 가로열 찾기
    max_value = 0
    for r in range(100):
        for c in range(100):
            word_list = []
            for i in range(100-c):
                if matrix[r][c:c+i+1] == matrix[r][c:c+i+1][::-1]:
                    length = len(matrix[r][c:c+i+1])
                    if max_value < length:
                        max_value = length

                word_list.append(matrix[c+i][r])
                if word_list == word_list[::-1]:
                    if max_value < len(word_list):
                        max_value = word_list

    print(f'#{tc} {max_value}')





