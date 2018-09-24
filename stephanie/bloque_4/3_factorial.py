numero = input("Ingresa un numero: ")

factorial = 1
numero = int(numero)
for contador in range(1, numero + 1):
    factorial = factorial*contador

print("El factorial de {0} es: {1}".format(numero, factorial))

# 5! = 5 x 4 x 3 x 2 x 1
'''
contador = 1
factorial = factorial x 1
contador 2
factorial = factorial x 2
contador 3
factorial = factorial x 3
contador 4
factorial = factorial x 3
contador 5
factorial = factorial x 5
'''
