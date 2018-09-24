##Dado un monto en soles, conviértelo a dólares y a euros.

monto  = input('Ingresa un monto \n')  
monto = float(monto)

monto_dol = monto*3.30
monto_eur = monto*3.88

print("El monto ingresado en dolares es: "+str(monto_dol) +" \n")
print("El monto ingresado en euros es: "+str(monto_eur))