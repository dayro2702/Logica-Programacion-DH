frutas = [1, "Fresas", True, 34.097] #Lista
numeros = (1,2,3,4,5) #Tupla

for i in frutas:
    print(i)

print(frutas[1])
print(len(frutas))
frutas[0] = "Banano" #Modificar una posicion 
print(frutas)
frutas.append("Mora") #Agregar un elemento al finla de la lista
print(frutas)
frutas.pop(2) #Elimina un elemento de la lista
print(frutas)
frutas.insert(2,"Kiwi") #Insertar un elemento en una posicion especifica
print(frutas)
frutas.remove("Fresas") #Elimina un elemento por su valor
print(frutas)

print(frutas[-1]) #Sacar el ultimo elemento fuera de la lista 
print(frutas[1:3]) #Imprime el elemento 1 y 2 de la lista (Slice)
print(frutas[::-1]) # Invierte el orden de los elementos
print(frutas[::2]) #Hace saltos de dos en dos 