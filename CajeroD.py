saldo = 1000000
ejecutando = True

print("Bienvenido al cajero en Python")

while ejecutando:
    print("---MENU PRINCIPAL---")
    print(f"El saldo actual es: {saldo}")
    print("1. Retirar Dinero")
    print("2. Consignar Dinero")
    print("3. Salida")
    
    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        try:
            monto = int(input("Ingrese el monto a retirar: "))
            if monto > saldo:
                print("Saldo insuficiente")
            elif monto < 0:
                print("No se puede retirar cantidades negativas")
            else:
                saldo -= monto
                print("Retiro exitoso.")
        except ValueError:
            print("Error: Ingrese numeros")
    elif opcion == "2":
        try:
            monto = int(input("Ingrese el monto a consignar: "))
            if monto > 0:
                saldo += monto
                print("Consignacion exitosa.")
            else:
                print("El monto debe ser positivo")
        except ValueError:
            print("Error: Ingrese solo numeros")
    elif opcion == "3":
        print("Gracias por usar nuestros servicios, hasta luego.")
        ejecutando = False
    else:
        print("Opcion invalida, intente de nuevo")   