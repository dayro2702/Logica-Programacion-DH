def sumar(): #def (definir una funcion)
    #Aqui empieza el codigo de mi funcion
    print("El resultado es", 5+5)

sumar() #Llamar una funcion

def restar(numero1, numero2):
    resultado = numero1 - numero2
    print("Este es el resultado de la resta:", resultado) #Reusar la logica
    
restar(10, 7)

lista = []
def agregar_elemento(balon):
    lista.append(balon)
    print(f"Se agrego, {balon} a la lista {lista}")

agregar_elemento("Balon")

#============================================
"""
UPPER: TODO EN MAYUSCULAS 
LOWER: todo a minusculas
CAPITALIZE: La Primera Letra De Cada Palabra En Mayuscula
TITLE: La primera letra de una frase en mayuscula
"""
concesionario = [
    {"marca": "Toyota", "modelo": "Corolla", "precio": 110},
    {"marca": "Mazda", "modelo": "CX-3", "precio": 90},
    {"marca": "Renault", "modelo": "Logan", "precio": 80}
]

def buscar_vehiculo(lista_carros, marca_busqueda):
    for carro in lista_carros:
        if carro["marca"].lower() == marca_busqueda.lower(): 
            return carro
    return None

carro = input("Ingrese la marca a buscar: ")
resultado = buscar_vehiculo(concesionario, carro)

if resultado != None:
    print(f"Vehiculo encontrado: Marca: {resultado["marca"]}, Modelo:{resultado["modelo"]}")
else:
    print("Vehiculo no encontrado")