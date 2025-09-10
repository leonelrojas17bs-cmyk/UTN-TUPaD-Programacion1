import random

print("Bienvenido al Bingo")
numeros = random.sample(range(1, 51), 25)
carton = [numeros[i:i+5] for i in range(0, 25, 5)]

def mostrar_carton(carton):
    for fila in carton:
        print([f"{num:2}" for num in fila])

mostrar_carton(carton)

sorteados = set()
while True:

    while True:
        numero = random.randint(1, 50)
        if numero not in sorteados:
            sorteados.add(numero)
            break

    print(f"\nSe sortea el número... {numero}", end=" -> ")
    encontrado = False
    for i in range(5):
        for j in range(5):
            if carton[i][j] == numero:
                carton[i][j] = 0
                encontrado = True
    if encontrado:
        print("¡Lo tenés!")
    else:
        print("No está en tu cartón.")

    mostrar_carton(carton)

    if all(num == 0 for fila in carton for num in fila):
        print("\n¡Bingo! Tu cartón quedó en:")
        mostrar_carton(carton)
        break