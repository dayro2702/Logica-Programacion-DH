diccionarios = {
    "id": 1,
    "nombre": "Dayro"
}

print("Estoy imprimiendo el valor de una llave",diccionarios["nombre"])
diccionarios["apellido"] = "Henao" #Agregar un dato nuevo
print("Agregar una llave al diccionario", diccionarios)

diccionarios["nombre"] = "Pepito" #Usando llave existente, se modifica el valor
print("Imprimir diccionario modificado", diccionarios)

del diccionarios["apellido"] #Esto elimina un elemento
print("Eliminando un elemento del diccionario", diccionarios)

estudiante = {
    "nombre": "Anna",
    "edad": 22,
    "nota": 4.8,
    "aprobada": True,
    "materias": ["Programacion", "Logica", "Metodologia"]
}

print(estudiante)
print("Imprimiendo la materia (Logica)", estudiante["materias"][1])
print("Imprimiendo las materias", estudiante["materias"])
estudiante["asistencia"] = {
    "Clase1": [0, 1, 1],
    "Clase2": [1, 1, 1]
}
print("Imprimiendo un diccionario dentro de otro diccionario", estudiante)

for key, value in estudiante.items(): # items (saca cada par de llaves y los separa por llaves y valores)
    print("Esta la llave:", key)
    print(f"Este es el valor {value} de la llave {key}")

print("Llaves del diccionario", estudiante.keys()) # .keys (Saca una lista con las llaves (nombre, edad, nota, aprobada, materias, asistencia))
print("Valores del diccionario", estudiante.values()) # .values (Saca lista con valores (Anna, 22, 4.8, True, ["Programacion", "Logica", "Metodologia"], {"Clase1": [0, 1, 1],"Clase2": [1, 1, 1]}))

for i in estudiante.values(): #Imprime uno a uno los valores
    print(i)