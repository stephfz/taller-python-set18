##Calculo de hipotenusa
#lado_c

import math

#Para evitar el error TypeError: Can't convert 'float' object to str implicitly
##Cambiar a float


lado_a = 3
lado_b = 4

lado_a = float(lado_a)
lado_b = float(lado_b)


lado_c = math.sqrt(lado_a**2 + lado_b**2)

##str => toString o parsear a string

print("El valor de la hipotenusa es: "+str(lado_c))