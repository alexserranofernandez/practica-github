#Realiza el ejercicio del DNI que encontrarás en el Sway
tabla_letras="TRWAGMYFPDXBNJZSQVHLCKE"
lista_intentos=[]
dni_correctos=[]
dni_incorrectos=[]
continuar="s"
while continuar=="s":
    dni = input("Introduce el número de DNI (8 dígitos): ")   
    if len(dni)!=8:
        print("Error: El DNI debe tener exactamente 8 dígitos")
        lista_intentos.append(0)
        dni_incorrectos.append(dni)
    elif not dni.isnumeric():
        print("Error: El DNI debe ser numérico")
        lista_intentos.append(1)
        dni_incorrectos.append(dni)
    else:
        numero=int(dni)
        resto=numero%23
        if resto<0 or resto>22:
            print("Error: El resto obtenido no es válido")
            lista_intentos.append(2)
            dni_incorrectos.append(dni)
        else:
            letra=tabla_letras[resto]
            print(f"NIF completo: {dni}-{letra}")
            lista_intentos.append(3)
            dni_correctos.append(dni)
    continuar=input("¿Deseas calcular otro DNI? (s/n):")
print("MENÚ")
print("1. Listar DNI correctos ordenados de menor a mayor")
print("2. Listar DNI incorrectos ordenados de menor a mayor")
print("3. Número total de errores")
print("4. Número total de DNIs correctos")
print("5. Porcentajes de DNIs")
print("6. Salir")
opcion=input("Selecciona una opción (1-6):")
if opcion=="1":
    dni_correctos.sort()
    print("DNI correctos ordenados:")
    for dni in dni_correctos:
        resto=int(dni) % 23
        letra=tabla_letras[resto]
        print(f"{dni}-{letra}")
elif opcion=="2":
    dni_incorrectos.sort()
    print("DNI incorrectos ordenados:")
    for dni in dni_incorrectos:
        print(dni)
elif opcion=="3":
    total_errores=0
    for codigo in lista_intentos:
        if codigo!=3:
            total_errores = total_errores+1
    print(f"Número total de errores:{total_errores}")
elif opcion=="4":
    total_correctos=0
    for codigo in lista_intentos:
        if codigo==3:
            total_correctos=total_correctos+1
    print(f"Número total de DNIs correctos:{total_correctos}")
elif opcion=="5":
    total=len(lista_intentos)
    errores_longitud=0
    errores_numerico=0
    errores_resto=0
    correctos=0
    for codigo in lista_intentos:
        if codigo==0:
            errores_longitud=errores_longitud+1
        elif codigo==1:
            errores_numerico=errores_numerico+1
        elif codigo==2:
            errores_resto=errores_resto+1
        elif codigo==3:
            correctos=correctos+1
    if total>0:
        porc_correctos=(correctos/total)*100
        porc_incorrectos=((errores_longitud+errores_numerico+errores_resto)/total)*100
        porc_longitud=(errores_longitud/total)*100
        porc_numerico=(errores_numerico/total)*100
        porc_resto=(errores_resto / total)*100
        print(f"% DNIs correctos: {round(porc_correctos, 1)}%")
        print(f"% DNIs incorrectos: {round(porc_incorrectos, 1)}%")
        print(f"% Errores de longitud: {round(porc_longitud, 1)}%")
        print(f"% Errores de número: {round(porc_numerico, 1)}%")
        print(f"% No existentes (resto inválido): {round(porc_resto, 1)}%")
    else:
        print("No se han introducido DNIs")
elif opcion=="6":
    print("Saliendo del programa...")

else:
    print("Opción no válida")
print("Programa finalizado")