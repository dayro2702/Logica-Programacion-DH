print(" Asistente Médico\n")

try:
    
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    temperatura = float(input("Temperatura (°C): "))

    print("Responde con 'si' o 'no':")

    respirar = input("¿Dificultad para respirar? ").lower()
    pecho = input("¿Dolor en el pecho? ").lower()
    sangrado = input("¿Sangrado abundante? ").lower()
    vomitos = input("¿Vómitos constantes? ").lower()
    dolor = input("¿Dolor fuerte? ").lower()


    if (respirar == "si" or pecho == "si") and temperatura >= 38:
        
        if temperatura >= 39 and edad > 60:
            print("DEBE IR A URGENCIAS (ALTO RIESGO)")
        else:
            print("DEBE IR A URGENCIAS")

    else:
        if (vomitos == "si" and dolor == "si") or temperatura >= 38:
            
            if edad < 5 and temperatura >= 38:
                print("DEBE TENER UNA CONSULTA PRIORITARIA (niño con fiebre)")
            else:
                print("DEBE TENER UNA CONSULTA PRIORITARIA")
        
        else:
            print("Puede quedarse en CASA")

except:
    print("ingresaste un dato inválido. Reinicia el programa.")