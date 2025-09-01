abecedario = list("abcdefghijklmnñopqrstuvwxyz")
corrimiento = int(input("ingrese el corrimiento:"))
for i in range(5):
    mensaje = input(f"ingrese el mensaje {i+1}: ").lower()
    mensaje_cifrado = ""
    for letra in mensaje:
        if letra in abecedario:
            indice = abecedario.index(letra)
            nuevo_indice = (indice + corrimiento) % len(abecedario)
            mensaje_cifrado += abecedario[nuevo_indice]
        else:
            mensaje_cifrado += letra
    print(f"mensaje cifrado {i+1}: {mensaje_cifrado}")
print("fin del programa")