n = int(input("Ingresa un numero: "))

acc = 1
i = 1
while i <= n:
    acc = acc*i
    i += 1

print("El factorial es: " + str(acc))

# Alternative: recursion