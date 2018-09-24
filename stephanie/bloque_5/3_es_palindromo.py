def palabra_palindromo(palabra):
    palabra_reves = ''

    contador = len(palabra) -1
    while (contador >= 0):
        palabra_reves = palabra_reves + palabra[contador]
        contador = contador - 1
    return palabra == palabra_reves




palabra = input("Ingresa una palabra: ")
es_palindromo =palabra_palindromo(palabra)
if (es_palindromo):
    print("Es Palindromo!")
else:
    print("No es Palindromo ")
