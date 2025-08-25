#indico los días válidos
dias_validos = ["lunes", "martes", "miercoles", "jueves", "viernes"]
mm_validos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11, 12]
dd_validos = list(range(1,32))
#Pido el ingreso de datos
fecha = input("Porfavor ingrese la fecha actual(dia, DD, MM) ").lower()
dia, fecha_incompleta = fecha.split(", ")
dd, mm = fecha_incompleta.split("/")
dd= int(dd)
mm= int(mm)
if dia in dias_validos:
    if dd in dd_validos:
        if mm in [1, 3, 5, 7, 8, 10, 12]:
            if 1 <= dd <= 31:
                print("correcto")
            else:
                print("dia incorrecto para el mes")
                exit()
        elif mm in [4, 6, 9, 11]: 
            if 1 <= dd <= 30:
                print("correcto")
            else:
                print("dia incorrecto para el mes")
                exit()
        elif mm == 2: 
            if 1 <= dd <= 28:
                print("correcto")
            else:
                print("dia incorrecto para el mes")
                exit()
        else:
            print("mes incorrecto")
            exit()
    else:
        print("dia del mes invalido")
        exit()
else:
    print("dia de la semana incorrecto")
    exit()
    
if dia in ["lunes"]:
    respuesta = input("¿Hubo examen en nivel inicial? (si/no):").lower()
    if respuesta == "si":
       aprobados = int(input("¿Cuantas personas aprobaron?"))
       desaprobados = int(input("¿Cuantos desaprobados hubieron?"))
       total = aprobados + desaprobados 
       if total > 0: 
           porcentaje_aprobados = (aprobados/total) * 100
           print(f"El porcentaje de aprobados fue de: {porcentaje_aprobados}")
       else: 
           print("no se registraron alumnos")
    else:
        print("No hubo examen el dia de hoy")
        exit()
elif dia in ["martes"]:
    respuesta = input("¿Hubo examen en nivel intermedio? (si/no):").lower()
    if respuesta == "si":
       aprobados = int(input("¿Cuantas personas aprobaron?"))
       desaprobados = int(input("¿Cuantos desaprobados hubieron?"))
       total = aprobados + desaprobados 
       if total > 0: 
           porcentaje_aprobados = (aprobados/total) * 100
           print(f"El porcentaje de aprobados fue de: {porcentaje_aprobados}")
       else: 
           print("no se registraron alumnos")
    else:
        print("No hubo examen el dia de hoy")
        exit()
elif dia in ["miercoles"]:
    respuesta = input("¿Hubo examen en nivel avanzado? (si/no):").lower()
    if respuesta == "si":
       aprobados = int(input("¿Cuantas personas aprobaron?"))
       desaprobados = int(input("¿Cuantos desaprobados hubieron?"))
       total = aprobados + desaprobados 
       if total > 0: 
           porcentaje_aprobados = (aprobados/total) * 100
           print(f"El porcentaje de aprobados fue de: {porcentaje_aprobados}")
       else: 
           print("no se registraron alumnos")
    else:
        print("No hubo examen el dia de hoy")
        exit()
elif dia in ["jueves"]: 
    asistencia = int(input("ingrese el porcentaje de asistencia a practica hablada:"))
    if asistencia > 50: 
        print("asistio la mayoria")
        exit()
    else:
        print("no asistio la mayoria")
        exit()
elif dia in ["viernes"]: 
    if dd == 1 and mm == 1 or 7:
        alumnos = int(input("ingrese la cantidad de alumnos del nuevo ciclo:"))
        arrancel = int(input("ingrese el arrancel por alumnos"))
        ingreso_total = alumnos * arrancel
        print(f"el ingreso total es:{ingreso_total}")
        exit()
    else:
        print("el dia de hoy se dicto ingles para viajeros")
        exit()