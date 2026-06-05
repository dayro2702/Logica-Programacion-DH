cantidad_de_productos = int(input("Ingrese cantidad de productos a registrar: "))
nombres_producto = []
cantitades_stock = []


for i in range(cantidad_de_productos):
    nombre = input(f"Ingrese el nombre del producto {i+1}: ")
    stock = int(input(f"Ingrese el stock de {nombre}: "))

    nombres_producto.append(nombre)
    cantitades_stock.append(stock)

    suma_stock = 0

print("---ESTADO DEL INVENTARIO---")
for i in range(cantidad_de_productos):
    nombre = nombres_producto[i]
    stock = cantitades_stock[i]

    if stock == 0:
        print(f"{nombre}: Critico")
    elif stock < 5:
         print(f"{nombre}: stock bajo [{stock}]")
    elif stock > 20:
        print(f"{nombre}: Stock excedente")
    else:
        print(f"{nombre}: Stock saludable")

promedio_stock = suma_stock / cantidad_de_productos

print("---RESULTADOS FINALES---")
print("Total productos:", cantidad_de_productos)
print("Promedio stock:", promedio_stock)
