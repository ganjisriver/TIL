def triangle(s):
    angle = []
    line = []
    for i in range(s):
        angle.append(1)
        line.append(1)
        if i < 2:
            pass
        else:
            for j in range(1, len(angle)-1):
                line[j] = angle[j-1] + angle[j]

        for j in range(len(angle)):
            angle[j] = line[j]
            print(angle[j], end=' ')
        print()

TC = int(input())
for tc in range(1, TC+1):

    n = int(input())
<<<<<<< HEAD
    triangle(n)
=======
    triangle(n)
>>>>>>> 7a996084a1a27ad6d1c9f62d1d7ad998111e3fc6
