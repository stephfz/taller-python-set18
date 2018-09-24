
contador = 1
num_primos=0
while (contador <= 20):
    divisibles = 0
    i = 1
    while (i <= contador):
        if contador % i == 0:
            divisibles+=1
        i+=1
    if divisibles == 2:
        num_primos+=1
    contador +=1
    
print("Entre 1 y 20 hay {0} numeros primos".format(num_primos))
