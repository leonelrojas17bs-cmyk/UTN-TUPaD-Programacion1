#ejercicio1
numerosmul4 = [n for n in range(1, 101) if n % 4 == 0]
print(numerosmul4)
#ejercicio2
lista5elementos= ["utn", 4, True, -3.3333, "nose"]
print(lista5elementos[3])
#ejercicio3
listavacia = []
listavacia.append(3)
listavacia.append("utn")
listavacia.append(False)
print(listavacia)
#ejercicio4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)
#ejercicio5
#el programa agarra el numero más alto de la lista con la función max y seguidamente lo remueve con numeros.remove
#ejercicio6
listaunoaltreinta = [n for n in range(10, 31, 5)]
print(listaunoaltreinta[0:2])
#ejercicio7
autos = ["sedan", "polo", "suran", "gol"] 
autos = ["sedan", "polo", "suran", "gol"]
nuevos = ["fiesta", "cruze"]

for i in range(1, 3):
    autos[i] = nuevos[i-1]
print(autos)
#ejercicio8
dobles = []

dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print(dobles)
#ejercicio9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], 
["agua"]]
compras[2].append("jugo")
print(compras)
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)
#ejercicio10
listaanidada = [[15], [True], [25.5, 57.9, 30.6], [False]]
print(listaanidada)