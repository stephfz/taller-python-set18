inicio = input("Desde que numero quieres contar? ")
fin = input("Hasta que numero quieres contar?: ")

contador = int(inicio)
fin = int(fin)
num_pares = 0

while(contador <= fin):
    if contador%2 == 0:
        num_pares +=1
    contador +=1    

print ("Numeros pares entre {0} y {1}: {2}".format(inicio,fin,num_pares))
