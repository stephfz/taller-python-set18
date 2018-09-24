
def suma(a,b):
    suma = a+b
    print("Suma: {0}".format(suma))

def resta(a,b):
    resta = a-b
    print("Resta: {0}".format(resta))

def multiplicacion(a,b):
    producto = a*b
    print("Multiplicacion: {0}".format(producto))

def division(a,b):
    division = a/b
    print("Division: {0}".format(division))

numero_a = input("Ingresa un numero: ")
numero_b = input("Ingresa otro numero: ")
a = int(numero_a)
b = int(numero_b)
suma(a,b)
resta(a,b)
multiplicacion(a,b)
division(a,b)
