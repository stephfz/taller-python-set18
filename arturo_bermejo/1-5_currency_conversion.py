amount = float(input("Ingresa el monto en soles: "))

usd_exchange_rate = 3.2
eur_exchange_rate = 3.88

usd_amount = amount/usd_exchange_rate
eur_amount = amount/eur_exchange_rate

print("El monto en dolares es: " + str(usd_amount))
print("El monto en euros es: " + str(eur_amount))
