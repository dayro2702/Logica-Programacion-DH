contraseña_correcta = "dh12345678"
intentos = 3

print("SISTEMA LOGIN")

try:
    contraseña = input("Ingrese la contraseña: ")

    if contraseña == contraseña_correcta:
        print("Bienvenido")

    else:
        intentos = intentos - 1
        print("Contraseña incorrecta")
        print("Intentos restantes: ", intentos)

        contraseña = input("Ingrese la contraseña: ")
        if contraseña == contraseña_correcta:
            print("Bienvenido")

        else:
            intentos = intentos - 1
            print("Contraseña incorrecta")
            print("Intentos restantes: ", intentos)

            contraseña = input("Ingrese la contraseña: ")
            if contraseña == contraseña_correcta:
                print("Bienvenido")
            
            else: 
                intentos = intentos - 1
                print("Sistema bloqueado")

except: 
    print("Ocurrio un error")
