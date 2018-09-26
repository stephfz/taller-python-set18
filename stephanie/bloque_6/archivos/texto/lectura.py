archivo = open("archivo_secreto.txt","r")
mensaje = archivo.read()
print(mensaje)
archivo.close()
