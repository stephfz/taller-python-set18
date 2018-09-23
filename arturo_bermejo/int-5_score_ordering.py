n_students = int(input("Ingresa el numero de alumnos: "))

avgs = []

for i in range(n_students):
    student = input("Nombre del alumno: ")
    scores = input("Notas (separado por comas): ")

    scores =  [int(score) for score in scores.split(',')]
    avg = round(sum(scores)/len(scores), 2)

    for j in range(len(avgs) + 1):
        if j == len(avgs):
            avgs.append([student, avg])
        elif avg > avgs[j][1]:
            avgs.insert(j, [student, avg])
            break

for avg in avgs:
    print("{} {}".format(avg[0], avg[1]))
