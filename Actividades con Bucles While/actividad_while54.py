#Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total 
#de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta 
#preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la 
#operación y su acumulado. Para aquellos de vosotros que os fijáis en los detalles, controlar que el 
#mensaje del acumulado es singular o plural. Con While
suma_total=0
operaciones_totales=0
while suma_total<50:
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