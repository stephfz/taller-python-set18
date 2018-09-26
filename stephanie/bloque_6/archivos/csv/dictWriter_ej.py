import csv

#Abrir el archivo para escritura
f = open('names.csv', 'w')

with f:
    fnames = ['nombre', 'apellido']
    writer = csv.DictWriter(f, fieldnames=fnames)
    writer.writeheader()
    writer.writerow({'nombre' : 'John', 'apellido': 'Smith'})
    writer.writerow({'nombre' : 'Robert', 'apellido': 'Brown'})
    writer.writerow({'nombre' : 'Julia', 'apellido': 'Griffin'})
f.close()
