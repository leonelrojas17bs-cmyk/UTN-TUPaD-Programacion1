def adivinar(letra, listSec, listOc):
    resultado = listOc
    for i in range(len(listSec)):
        if letra == listSec[i]:
            listOc[i] = letra
    return lista_actualizada(resultado, listOc)

def lista_actualizada(resultado, listOc):
    for i in range(len(listOc)):
        print(listOc[i], end=" ")
    print()
    return resultado

import random

lista_palabras = (
    "computacion", "ciberseguridad", "placa", "microchip",
    "tarjeta", "tecnicatura", "programacion", "resonancia",
    "walter", "albuquerque"
)

while True:
    palabra_secreta = random.choice(lista_palabras)
    palabra_oculta = "_" * len(palabra_secreta)
    lista_secreta = list(palabra_secreta)
    lista_oculta = list(palabra_oculta)
    intentos = 9

    print("\nBienvenido al juego del AHORCADO!")
    print("Tiene 6 intentos. Si los excede, PIERDE.")
    print(f"Atento! La palabra es: {palabra_oculta}")

    while True:
        if "_" not in lista_oculta:
            print("FIN DEL JUEGO, ¡GANÓ!")
            print(f"La palabra secreta era: {palabra_secreta}")
            break
        if intentos == 0:
            print("FIN DEL JUEGO, PERDIÓ")
            print(f"La palabra secreta era: {palabra_secreta}")
            break

        letra = input("Ingrese una letra: ").lower()
        if letra.isalpha() and len(letra) == 1:
            retorno = adivinar(letra, lista_secreta, lista_oculta)
            intentos -= 1
        else:
            print("Debe ingresar un solo caracter válido.")

    # Preguntar si desea continuar
    while True:
        opc = input("¿Desea continuar? Ingrese S para continuar o N para salir: ").strip()
        if len(opc) == 1 and (opc == "S" or opc == "s"):
            print("Preparando el siguiente juego...")
            break  # rompe solo el bucle de la pregunta, no el principal
        elif len(opc) == 1 and (opc == "N" or opc == "n"):
            print("ADIOS")
            exit()  # sale del programa completamente
        else:
            print("Debe ingresar S o N.")
