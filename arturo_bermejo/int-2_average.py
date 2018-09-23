m = int(input("Ingresa la cantidad de valores: "))

number_list = []

i = 0
while i < m:
    n = int(input("Ingresa un numero: "))
    number_list.append(n)
    i += 1

avg = sum(number_list)/len(number_list)

print("El promedio es: " + str(avg))
