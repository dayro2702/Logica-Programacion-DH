def celcius_fahrenhit(celcius):
    resultado = (celcius * 9/5) + 32
    return resultado

def celcius_kelvin(celcius):
    resultado = celcius + 273.15
    return resultado

celcius = int(input("Ingrese la cantidad de grados Celcius: "))
pregunta = int(input("Ingrese la opcion que quiere usar, 1. Celcius a Fahrenhit o 2. Celcius a Kelvin "))

if pregunta == 1:
    resultado_operacion = celcius_fahrenhit(celcius)
elif pregunta == 2:
    resultado_operacion = celcius_kelvin(celcius)
else:
    print("Opcion no valida")

print(resultado_operacion)