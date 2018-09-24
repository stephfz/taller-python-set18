inicio = input("Desde que numero quieres contar? ")
fin = input("Hasta que numero quieres contar?: ")

inicio = int(inicio)
fin = int(fin)
for contador in range(inicio, fin):
    print(contador)
