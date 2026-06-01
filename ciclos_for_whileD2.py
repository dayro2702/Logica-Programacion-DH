print("========"*3)

for i in range(0,20,2):
    print(i)

print("===WHILE===")

num_final = int(input("Ingrese un numero: "))


contador = 100
while(contador >= num_final):
    print(contador)
    contador -= 1 # contador = contador + 1

print("Tablas de multiplicar")

multiplicar = int(input("Ingrese el numero de la tabla a generar"))
for i in range(11):
    res = multiplicar * i 
    print(f"{multiplicar} X {i} = {res}")

print("===Caja registradora===")
cantidad_productos = int(input("Ingrsese el numero de productos"))

total = 0

for i in range(cantidad_productos):
    precio_productos = int(input(f"Ingrese el precio de cada producto {i}: "))
    total += precio_productos

print(f"La suma total de los productos es: ", total)

print("Resultado while")
total = 0
cortador = 1
while (contador <= cantidad_productos):
    precio_productos = int(input(f"Ingrese el precio de cada producto {contador}: "))
    total += precio_productos
    contador += 1
print("El precio total es: ", total)