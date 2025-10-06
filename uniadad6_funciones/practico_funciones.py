#ACTIVIDAD 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

#ACTIVIDAD2
def saludar_usuario(name):
    print(f"Hola {name}!")
    
nombre = input("ingrese su nombre ")
saludar_usuario(nombre)

#ACTIVIDAD3
def informacion_personal(nom, apl, edad, res):
    print(f"Mi nombre es {nom} {apellido}, tengo {edad} años y vivo en {res}")

nombre = input("Ingrese su nombre ")
apellido = input("Ingrese su apellido ")
edad = int(input("Ingrese su edad "))
residencia = input("Ingrese su residencia ")
informacion_personal(nombre, apellido, edad, residencia)

#ACTIVIDAD4
def calcular_area(rad):
    area = 3.14 *(radio**2)
    return area
def calcular_perimetro(rad):
    perimetro = 2 * 3.14 * radio
    return perimetro

radio = float(input("Ingrese el radio del circulo"))
area = calcular_area(radio)
perimetro = calcular_perimetro(radio)

print(f"AREA: {area}")
print(f"PERIMETRO: {perimetro}")

#ACTIVIDAD5
def segundos_a_horas(seg):
    horas = segundos/3600
    return horas

segundos = int(input("Ingrese la cantidad de segundos"))
horas = segundos_a_horas(segundos)
print(horas)

#ACTIVIDAD6
def tabla_mul(num):
    for i in range(1, 11):
        resultado = num*i
        print(f"{num} * {i} = {resultado}")

numero = int(input("Ingrese un número para mostrar la tabla de multiplicar"))
tabla_mul(numero) 

#ACTIVIDAD7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = None
    if b != 0:
        division = a / b
    else:
        division = "No se puede dividir entre cero"
    return (suma, resta, multiplicacion, division)

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

resultados = operaciones_basicas(a, b)

print("\nResultados de las operaciones básicas:")
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

#ACTIVIDAD8

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso, altura)

print(f"Su índice de masa corporal (IMC) es: {imc}")

#ACTIVIDAD9

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Ingrese la temperatura en grados Celsius: "))

resultado = celsius_a_fahrenheit(celsius)

print(f"{celsius}°C equivalen a {resultado}°F")

#ACTIVIDAD10

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

resultado = calcular_promedio(a, b, c)

print(f"El promedio de los tres números es: {resultado}")
