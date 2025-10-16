#EJERCICIO1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
1450} 
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300
precios_frutas.update({"Banana": 1330, "Manzana": 1700, "Melón": 2800})
lista_frutas = list(precios_frutas.keys())
print(precios_frutas)
print(lista_frutas)
#EJERCICIO2
contactos = {}

for i in range(5):
    while True:
        try:
            nombre = input("Ingrese el nombre del contacto: ").capitalize().strip()
            if not nombre:
                raise ValueError("El nombre no puede estar vacío")
            numero = int(input("Ingrese el número del contacto: "))
        except ValueError as e:
            print("ERROR:", e)
            continue
        else:
            contactos[i] = {"nombre": nombre, "numero": numero}
            break  # sale del while, pasa al siguiente contacto
validar = input("Ingrese el nombre del contacto para validar si existe: ").capitalize().strip()

encontrado = False
for datos in contactos.values():
    if datos["nombre"] == validar:
        encontrado = True
        break

if encontrado:
    print("El contacto está en la lista.")
else:
    print("El contacto no está en la lista.")

#EJERCICIO3

frase = input("Escribe una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

contador_palabras = {}
for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1

print("Cantidad de veces que aparece cada palabra:", contador_palabras)

#EJERCICIO4
alumnos = {}

for i in range(3):
    while True:
        try:
            nombre = input("Ingrese el nombre del alumno: ").capitalize().strip()
            if not nombre:
                raise ValueError("El nombre no puede estar vacío")
            notas_lista = []
            for j in range(3):
                nota = float(input(f"Ingrese la nota {j+1} de {nombre}: "))
                if nota < 0 or nota > 10:
                    raise ValueError("La nota debe estar entre 0 y 10")
                notas_lista.append(nota)

            alumnos[nombre] = tuple(notas_lista)

        except ValueError as e:
            print("ERROR:", e)
        else:
            break

print("Diccionario de alumnos con notas:")
print(alumnos)
print("\nPromedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

#EJERCICIO5

parcial1 = {"Ana", "Juan", "Luis", "Marta"}
parcial2 = {"Luis", "Marta", "Pedro", "Lucía"}

ambos = parcial1 & parcial2
print("Aprobó ambos parciales:", ambos)

solo_uno = (parcial1 - parcial2) | (parcial2 - parcial1)
print("Aprobó solo uno de los parciales:", solo_uno)

al_menos_uno = parcial1 | parcial2
print("Aprobó al menos un parcial:", al_menos_uno)

#EJERCICIO6

lista_productos = {
    "aceite": 3,
    "arroz": 5,
    "huevos": 48,
    "pan": 0
}

while True:
    print("INGRESE QUE DESEA HACER:")
    print("1: consultar stock de producto")
    print("2: agregar stock a producto")
    print("3: agregar producto")
    print("4: SALIR")

    while True:
        try:
            opc = int(input())
        except ValueError:
            print("Debe ingresar un número")
        else:
            break

    match opc:
        case 1:
            while True:
                try:
                    nombre_producto = input("Ingrese el nombre del producto: ").strip().lower()
                    stock = lista_productos[nombre_producto]
                except KeyError:
                    print("El producto no está en la lista.")
                else:
                    print(f"El stock del producto es {stock}")
                    break
        case 2:
            while True:
                try:
                    nombre_producto = input("Ingrese el nombre del producto: ").strip().lower()
                    cantidad_a_agregar = int(input("Ingrese la cantidad a agregar: "))
                    lista_productos[nombre_producto] += cantidad_a_agregar
                except KeyError:
                    print("Error: el producto no está en la lista.")
                except ValueError:
                    print("Debe ingresar un número entero")
                else:
                    print(f"Nuevo stock de {nombre_producto}: {lista_productos[nombre_producto]}")
                    break
        case 3:
            nuevo_producto = input("Ingrese el nombre del producto: ").strip().lower()
            while True:
                try:
                    cantidad_inicial = int(input("Ingrese la cantidad inicial: "))
                    lista_productos[nuevo_producto] = cantidad_inicial
                except ValueError:
                    print("Debe ingresar un número entero")
                else:
                    print(f"Producto '{nuevo_producto}' agregado con stock {cantidad_inicial}")
                    break
        case 4:
            break
        case _:
            print("Debe ingresar un número de la lista")

#EJERCICIO7
agrenda = {
    ("lunes", "10:00"): "Reuníon",
    ("martes", "13:00"): "Trabajo",
    ("miercoles", "20:00"): "Doctor",
    ("jueves", "05:00"): "Escuela",
    ("viernes", "21:00"): "Cita"
}

while True:
    print("\nQué deseas hacer?")
    print("1: Consultar evento")
    print("2: Agregar evento")
    print("3: Ver todos los eventos")
    print("4: Salir")

    try:
        opcion = int(input())
    except ValueError:
        print("Debe ingresar un número")
        continue

    match opcion:
        case 1:
            dia = input("Ingrese el día: ").strip().lower()
            hora = input("Ingrese la hora (HH:MM): ").strip()
            clave = (dia, hora)
            if clave in agenda:
                print(f"Evento: {agenda[clave]}")
            else:
                print("No hay ningún evento en esa fecha y hora.")
        case 2:
            dia = input("Ingrese el día: ").strip().lower()
            hora = input("Ingrese la hora (HH:MM): ").strip()
            evento = input("Ingrese el nombre del evento: ").strip()
            clave = (dia, hora)
            agenda[clave] = evento
            print(f"Evento '{evento}' agregado para {dia} a las {hora}.")
        case 3:
            if agenda:
                for clave, evento in sorted(agenda.items()):
                    print(f"{clave[0].capitalize()} {clave[1]}: {evento}")
            else:
                print("No hay eventos en la agenda.")
        case 4:
            break
        case _:
            print("Opción no válida")
#EJERCICIO 8

paises_a_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "México": "Ciudad de México"
}

capitales_a_paises = {}

for pais, capital in paises_a_capitales.items():
    capitales_a_paises[capital] = pais

print(capitales_a_paises)
