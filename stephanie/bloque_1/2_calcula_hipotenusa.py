import math

lado_a = input("Ingresa el valor del lado A: ")
lado_b = input("Ingresa el valor del lado B: ")

lado_a = float(lado_a)
lado_b = float(lado_b)
suma_cuadradros = math.pow(lado_a,2) + math.pow(lado_b,2)
hipotenusa = math.sqrt(suma_cuadradros)

print("El valor de la hipotenusa es: {0}".format(hipotenusa))
