reemplazo = {'a': 1, 'e': 2, 'i':3,'o':4, 'u':5}
palabra = input("Ingrese una palabra: ")

longitud = len(palabra)
nueva_palabra = ''

for contador in range(longitud):
    letra = palabra[contador]
    if letra in reemplazo.keys():
        letra = str(reemplazo[letra])
    nueva_palabra = nueva_palabra + letra
    
print(nueva_palabra)
