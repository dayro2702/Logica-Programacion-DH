import csv

# Sistema de Control de Entrada - Eventos VIP
asistentes = []
cupo_maximo = 20

while True:

    print("--- EVENTO VIP ---")
    print("1. Registrar persona")
    print("2. Ver lista")
    print("3. Editar nombre")
    print("4. Eliminar persona")
    print("5. Ver estadísticas")
    print("6. Generar reporte")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        if len(asistentes) >= cupo_maximo:
            print("No hay más cupos disponibles.")

        else:
            nombre = input("Ingrese el nombre: ")

            if nombre in asistentes:
                print("Esa persona ya está registrada.")
            else:
                asistentes.append(nombre)
                print("Persona registrada correctamente.")

    elif opcion == "2":

        if len(asistentes) == 0:
            print("No hay personas registradas.")

        else:
            print("Lista de asistentes:")

            for i in range(len(asistentes)):
                print(i, "-", asistentes[i])

    elif opcion == "3":

        try:
            indice = int(input("Ingrese el número de la persona a editar: "))

            if indice >= 0 and indice < len(asistentes):

                nuevo_nombre = input("Ingrese el nuevo nombre: ")

                if nuevo_nombre in asistentes:
                    print("Ese nombre ya existe.")

                else:
                    asistentes[indice] = nuevo_nombre
                    print("Nombre actualizado correctamente.")

            else:
                print("Índice no válido.")

        except:
            print("Error. Debe ingresar un número.")

    elif opcion == "4":

        try:
            indice = int(input("Ingrese el número de la persona a eliminar: "))

            if indice >= 0 and indice < len(asistentes):

                eliminado = asistentes.pop(indice)
                print("Se eliminó a:", eliminado)

            else:
                print("Índice no válido.")

        except:
            print("Error. Debe ingresar un número.")

    elif opcion == "5":

        print("--- ESTADÍSTICAS ---")
        print("Personas registradas:", len(asistentes))
        print("Cupos disponibles:", cupo_maximo - len(asistentes))

    elif opcion == "6":

        if len(asistentes) == 0:
            print("No hay asistentes para generar reportes.")
        else:
            with open("reporte_asistencia.csv", mode="w", newline="") as archivo:
                escritor = csv.writer(archivo)

                escritor.writerow(["Numero", "Nombre"])

                for i in range(len(asistentes)):
                    escritor.writerow([i, asistentes[i]])
            
            print("Reporte generado correctamente: reporte_asistencia.csv")

    elif opcion == "7":

        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")