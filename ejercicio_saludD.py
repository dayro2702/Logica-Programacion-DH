ataques = [
    ["Normal", 20],
    ["Especial", 30],
]

salud_jefe = 100
energia = 50

for i in range(len(ataques)):

    ataque = ataques[i]

    try:
        tipo = ataque[0]
        daño = ataque[1]

    except:
        print("Ataque fallido")
        continue

    if daño > 0:

        if tipo == "Especial":

            if energia >= 20:

                salud_jefe -= daño * 2
                energia -= 20

                print(f"Ataque especial realizado")
                print(f"Daño causado: {daño * 2}")
                print(f"Energía restante: {energia}")

            else:
                print("Sin energía")

        else:

            salud_jefe -= daño

            print("Ataque normal realizado")
            print(f"Daño causado: {daño}")

    print(f"Salud restante del jefe: {salud_jefe}")
    print("---------------------------")

    if salud_jefe <= 0:
        print("¡Jefe Derrotado!")
        break

if salud_jefe > 0:
    print("El jefe sobrevive")