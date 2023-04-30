score_dict = {'A+':4.5,'A0':4.0,'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0}
전공총학점 = 72.0
취득학점 = 0
for i in range(23):
    과목점수 = input()
    if 과목점수 == 'PASS':
        전공총학점 -= 3
    else:
        취득학점 += score_dict[과목점수]
print(취득학점/전공총학점*3)