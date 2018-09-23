import math  # El modulo math nos permite hacer operaciones matematicas

# Obtenemos los valores de los lados
a = input("Lado a: ")
b = input("Lado b: ")

# Convertimos recibidos como cadenas a flotantes
a = float(a)
b = float(b)

# Realizamos el calculo y lo imprimimos
hypotenuse = math.sqrt(a*a + b*b)

print("La hipotenusa es : " + str(hypotenuse))
