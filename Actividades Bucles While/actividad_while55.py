#Última vez que reutilizamos el mismo código. A partir del programa anterior 
#haz que sea todo exactamente igual pero teniendo en cuenta que el programa se repita siempre y 
#cuando la suma acumulada sea superior a 50 o la suma acumulada sea par. Con While
suma_total=0
operaciones_totales=0
while suma_total<50 or suma_total//2==suma_total/2:
    var_numero1=int(input("Introduce un número:"))
    var_numero2=int(input("Introduce otro número:"))
    var_suma=var_numero1+var_numero2
    print(f"El resultado de la suma es {var_suma}")
    operaciones_totales=operaciones_totales+1
    suma_total=suma_total+var_suma
    if operaciones_totales==1:
        print(f"El total acumulado es {suma_total} y llevas {operaciones_totales} operación realizada.")
    else:
        print(f"El total acumulado es {suma_total} y llevas {operaciones_totales} operaciones realizadas.")
else:      
    print("Fin del programa")