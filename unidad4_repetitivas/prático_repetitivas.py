#ejercicio 1
for i in range(101):
    print(i)

#ejercicio 2
numero = int(input("Ingrese un número entero: "))
digitos = 0
temp = abs(numero)
if temp == 0:
    digitos = 1
else:
    while temp > 0:
        temp //= 10
        digitos += 1
print(f"Cantidad de dígitos: {digitos}")

#ejercicio 3
inicio = int(input("Ingrese el primer valor: "))
fin = int(input("Ingrese el segundo valor: "))
suma = 0
for i in range(inicio + 1, fin):
    suma += i
print(f"La suma de los números entre {inicio} y {fin} (excluyendo ambos) es: {suma}")

#ejercicio 4
total = 0
while True:
    num = int(input("Ingrese un número entero (0 para terminar): "))
    if num == 0:
        break
    total += num
print(f"Total acumulado: {total}")

#ejercicio 5
import random
numero_secreto = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1
    if intento == numero_secreto:
        print(f"¡Correcto! Lo lograste en {intentos} intentos.")
        break

#ejercicio 6
for i in range(100, -1, -2):
    print(i)

#ejercicio 7
n = int(input("Ingrese un número entero positivo: "))
suma = 0
for i in range(n + 1):
    suma += i
print(f"La suma de los números entre 0 y {n} es: {suma}")

#ejercicio 8
pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(100):
    num = int(input(f"Ingrese el número {i+1}: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")

#ejercicio 9

num = 0
media = 0
suma = 0

for i in range(100):
    num = int(input("ingrese 100 numeros: "))
    suma += num
media = suma/100

#ejercicio 10

#ejercicio 10

numero = int(input("Ingrese un número entero: "))
invertido = 0
while numero > 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero //= 10
print(f"Número invertido: {invertido}")