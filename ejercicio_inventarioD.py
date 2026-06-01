nombres_producto = []
cantitades_stock = []

try:
    cantidad_de_productos = int(input("Ingrese cantidad de productos a registrar: "))

    for i in range(cantidad_de_productos):
        nombre = input(f"Ingrese el nombre del producto {i+1}: ") # f (perimtir que una varible quede dentro del texto)

        while True:
            try:
                cantidad = int(input(f"Ingrese el stock de {nombre}: "))
                break
            except:
                print("Error: Ingrese un numero valido.")
        
        nombres_producto.append(nombre)
        cantitades_stock.append(cantidad)

    print("---ESTADO DEL INVENTARIO---")
    suma_stock = 0

    for i in range(len(nombres_producto)):
        nombre = nombres_producto[i]
        stock = cantitades_stock[i]
        suma_stock += stock  # suma_total = suma_total + stock

        if stock == 0:
            print(f"Critico: {nombre} Agotado.")
        else:
            if stock < 5:
                 print(f"ALERTA: {nombre}: stock bajo {stock} unidades")
            else:
                if stock > 20:
                    print(f"{nombre}: Stock excedente, aplicar descuento")
                else:
                    print(f"{nombre}: Stock saludable")

    promedio_stock = suma_stock / cantidad_de_productos

    print("---RESULTADOS FINALES---")
    print(f"Total productos: {cantidad_de_productos}\n")
    print(f"Promedio stock en bodega: {promedio_stock}")
except ValueError:
    print("Error: El numero de productos debe ser entero")