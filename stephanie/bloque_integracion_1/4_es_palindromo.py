palabra = input("Ingresa una palabra: ")

palabra_reves = ''

contador = len(palabra) -1
while (contador >= 0):
    palabra_reves = palabra_reves + palabra[contador]
    contador = contador - 1

if (palabra == palabra_reves):
    print("Es Palindromo!")
else:
    print("No es Palindromo ")    
