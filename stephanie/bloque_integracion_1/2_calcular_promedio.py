notas = [15,15,11,14,20,17]

tope = len(notas)
suma = 0
for i in range(0,tope):
    suma = suma + notas[i]
prom = suma / tope

print("Promedio : {0}".format(prom))
