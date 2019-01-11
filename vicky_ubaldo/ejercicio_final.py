##Ejercicio final

#Primer valor
numero1 = input('Ingresa el primer numero: ')
numero1=int(numero1)

#Segundo valor
numero2 = input('Ingresa el segundo numero: ')
numero2=int(numero2)


##Se valida que el segundo numero sea mayor que el primero 
while(numero2<numero1):
	numero2=0
	print('El segundo numero debe ser mayor que el primero!! ')
	numero2 = input('Ingresa el segundo numero: ')
	



##Fizz cuando el numero sea dividido entre 3
##Buz cuando el numero sea dividido entre 5
##Si es divisible entre 3 y 5 , FizzBuzz

def fizzbuzz(num):
	if num%3==0 and num%5==0:
		print("FizzBuzz")
	elif num%3==0 :
		print("Fizz")
	elif num%5==0:
		print("Buzz")
	else:
		return num

		
print('Primer numero '+str(numero1))
print('Segundo numero '+str(numero2))
fizzbuzz(int(numero1))
fizzbuzz(int(numero2))



 