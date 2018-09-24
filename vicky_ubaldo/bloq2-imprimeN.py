##Imprimir el elemento N de una lista. N es un valor ingresado por el usuario.

destinos= ['Huaraz','Cusco','Huancayo','Ica','Trujillo']

valor = input('Ingresa el valor de busqueda (1 al 5)')

## Errores
# TypeError: list indices must be integers or slices, not str
valor= int(valor)

print("El valor es: "+destinos[valor])