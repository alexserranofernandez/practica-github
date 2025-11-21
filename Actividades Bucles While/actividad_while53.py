#A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las 
#sumas y el número de repeticiones. Con While
suma_total=0
repeticiones_totales=0
repetición="s"
while repetición=="s":
    var_numero1=int(input("Introduce un número:"))
    var_numero2=int(input("Introduce otro número:"))
    var_suma=var_numero1+var_numero2
    print(f"El resultado de la suma es {var_suma}")
    repeticiones_totales=repeticiones_totales+1
    suma_total=suma_total+var_suma
    repetición=input("Desea repetir la operación s/n:")
else:
    print("Fin del programa. Resumen")
    print(f"La suma total es: {suma_total} y el número de repeticiones es: {repeticiones_totales}.")
    