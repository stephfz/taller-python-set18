import csv

#Abrir el archivo en modo lectura
f = open('valores.csv', 'r')

with f:
    reader = csv.DictReader(f)
    #por cada linea en el reader
    for row in reader:
        print(row['min'], row['avg'], row['max'])
