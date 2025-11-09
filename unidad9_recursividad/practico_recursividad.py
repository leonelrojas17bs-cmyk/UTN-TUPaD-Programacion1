#EJERCICIO1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Ingrese un número: "))

for i in range(1, num + 1):
    print(f"Factorial de {i} = {factorial(i)}")

#EJERCICIO2
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Ingrese la posición hasta la que desea ver la serie de Fibonacci: "))

for i in range(num):
    print(fibonacci(i), end=" ")

#EJERCICIO3
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base = int(input("Ingrese la base: "))
exp = int(input("Ingrese el exponente: "))

print(f"{base}^{exp} = {potencia(base, exp)}")

#EJERCICIO4
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

num = int(input("Ingrese un número decimal: "))
binario = decimal_a_binario(num)
print(f"El número {num} en binario es {binario if binario else '0'}")

#EJERCICIO5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    else:
        return palabra[0] == palabra[-1] and es_palindromo(palabra[1:-1])

texto = input("Ingrese una palabra: ").lower()
print(es_palindromo(texto))

#EJERCICIO6
def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + suma_digitos(n // 10)

num = int(input("Ingrese un número: "))
print(f"La suma de los dígitos es {suma_digitos(num)}")

#EJERCICIO7
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

niveles = int(input("Ingrese la cantidad de bloques en el nivel inferior: "))
print(f"Total de bloques necesarios: {contar_bloques(niveles)}")

#EJERCICIO8
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

num = int(input("Ingrese un número: "))
d = int(input("Ingrese el dígito a buscar (0-9): "))
print(f"El dígito {d} aparece {contar_digito(num, d)} veces en {num}")
