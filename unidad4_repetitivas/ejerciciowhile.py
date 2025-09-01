import random
opciones = ["piedra", "papel", "tijera"]
contador = 0
contador_ia = 0
salir = True

print("Bienvenido a piedra, papel o tijeras!")
while salir == True: 
    print("Porfavor escribe tu eleccion!:") 
    opcion = input("Piedra - Papel - Tijera - Salir ").lower()
    opcion_ia = random.choice(opciones)
    if opcion == "piedra": 
        if opcion_ia == "tijera":
            print("La pc eligio tijera")
            print("Ganas!")
            contador = contador + 1
        elif opcion_ia == "papel":
            print("La pc eligio papel")
            print("Pierdes!")
            contador_ia = contador_ia + 1
        else:
            print("La pc eligio piedra")
            print("Empate.")
    elif opcion == "papel":
        if opcion_ia == "piedra":
            print("La pc eligio piedra")
            print("Ganas!")
            contador = contador + 1
        elif opcion_ia == "tijera":
            print("La pc eligio tijera")
            print("Pierdes!")
            contador_ia = contador_ia + 1
        else:
            print("La pc eligio papel")
            print("Empate.")
    elif opcion == "tijera":
        if opcion_ia == "papel":
            print("La pc eligio papel")
            print("Ganas!")
            contador = contador + 1
        elif opcion_ia == "piedra":
            print("La pc eligio piedra")
            print("Pierdes!")
            contador_ia = contador_ia + 1
        else:
            print("La pc eligio tijera")
            print("Empate.")
    elif opcion == "salir":
        salir = False
        print(f"Marcador final - Tú: {contador} | IA: {contador_ia}")
        print("¡Gracias por jugar!")
        exit()