import csv

print("EXPORTADOR DE REPORTES")

#[] = Lista, () = Tupla, {} = Diccionario
equipos = [
    {"serie": "SN001", "marca": "Dell", "estado": "Operativo"},
    {"serie": "SN002", "marca": "Lenovo", "estado": "En mantenimiento"}
]

with open("reporte.csv", mode="w", newline="") as archivo: # w (write) = Escribir

    escritor = csv.writer(archivo)

    escritor.writerow({"Numero Serie", "Marca", "Estado Actual"}) # writerow (Que escriba en una sola fila)

    for equipo in equipos:
        escritor.writerow([equipo["serie"], equipo["marca"], equipo["estado"]])

print("Reporte generado existosamente")