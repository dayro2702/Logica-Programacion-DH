import csv

print("IMPORTADOR DE DATOS")

inventario = []

try:
    with open("reporte.csv", mode="r") as archivo:
        lector = csv.reader(archivo)

        for fila in lector:
            print(f"Cargando equipo: {fila[1]} (Serie: {fila[0]})")
            inventario.append(fila)
    print("Archivo leido correctamente")
    print(inventario)
except:
    print("Archivo no existe")