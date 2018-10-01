import csv

headers = ["Nombre", "Celular", "Email", "Distrito"]

def crear_nuevo_contacto():
    dicc = {}
    for k in headers:
        valor = input("{0} del contacto: ".format(k))
        dicc[k] = valor

    myFile = open("contactos.csv", 'a')
    with myFile:
        writer = csv.DictWriter(myFile, fieldnames=headers)
        writer.writerow(dicc)
    print("----Contacto Guardado----")


def leer_contactos():
    f = open('contactos.csv', 'r')
    contactos = []
    with f:
        reader = csv.DictReader(f)
        for row in reader:
            contacto = {}
            for h in headers:
                contacto[h] = row[h]
            contactos.append(contacto)
    return contactos

def buscar_contacto(nombre):
    libreta = leer_contactos()
    contacto ={}
    for entrada in libreta:
        nom = entrada["Nombre"]
        if nom == nombre:
            contacto = entrada
            break
    if bool(contacto):
        imprimir_contacto(contacto)
    else:
        print ("El contacto {0} no existe".format(nombre))


def imprimir_contacto(contacto):
    print("**Informacion del Contacto**")
    for key in contacto.keys():
        print("{0} : {1}".format(key, contacto[key]))
    print("****************************")

def contactos_por_distrito(distrito):
    contactos = 0
    libreta = leer_contactos()
    for entrada in libreta:
        d = entrada["Distrito"]
        if d == distrito:
            contactos +=1
    print("Tienes {0} contacto(s) en el distrito {1}".format(contactos,distrito))        




opcion = ''
# N nuevo contacto
# B buscar contacto
# T terminar programa
while (opcion != 'T'):
    print("---------------------")
    print("Que deseas hacer?")
    print("[N] nuevo contacto")
    print("[B] buscar contacto")
    print("[D] contactos por distrito")
    print("[T] terminar programa")
    opcion = input("Ingresa tu opcion: ").upper()
    if opcion == 'N':
        crear_nuevo_contacto()
    if opcion == 'B':
        nombre = input("Nombre de contacto a buscar: ")
        buscar_contacto(nombre)
    if opcion == 'D':
        distrito = input("En que distrito quieres buscar? ")
        contactos_por_distrito(distrito)
