#actividad de ejercicios complementarios unidad2
#ejercicio numero 1

numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
suma= numero1+numero2
resta= numero1-numero2
multiplicacion= numero1*numero2
division= numero1/numero2
print(f"la suma es de los dos numeros es: {suma}")
print(f"la resta de los dos numeros es: {resta}")
print(f"la multiplicacion de los dos numeros es: {multiplicacion}")
print(f"la division de los dos numeros es: {division}")

#ejercicio descuento y nombre

nombre = input("Ingresa tu nombre: ")
precio = float(input("Ingresa el precio del producto: "))
descuento= 0.50
precio_final= precio*descuento
print(f"hola {nombre}, tiene un descuento de: {precio_final}")

#ejercicio longitud cadena

cadena= input("ingrese una cadena ")
longitud = len(cadena)
print(longitud)

#ejercicio convertir a entero

precio= float(input("ingrese un numero con decimales: "))
precio= int(precio)
print(precio)

#ejercicio nombre + apellido

nombre2= "leonel"
apellido= "rojas"
nombre_completo= nombre2 + " " + apellido
print(f"{nombre_completo}")

#ejercicio edad y altura modificadas

edad= 18
edad= edad + 5
edad= edad - 10
altura= 1.64
altura= (altura*4)/3
print(f"altura: {altura} edad: {edad}")

#nombre a mayusculas y nombre primera letra 

nombremay= "LEONEL ROJAS"
nombremin= nombremay.lower()
nombreprimermay= nombremin.capitalize()
print(f"nombre en minusculas: {nombremin} nombre arreglado: {nombreprimermay}")

#fin de la actividad