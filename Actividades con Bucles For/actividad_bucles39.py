#Programa que pida n números y que, tras introducir el último número, debe aparecer por 
#pantalla el número total de positivos, negativos y número de 0.
var_repeticiones=int(input("Introduce el número de números que quieres introducir:"))
var_0=0
var_positivos=0
var_negativos=0
for i in range(var_repeticiones):
    var_número=int(input("Introduce un número:"))
    if var_número>0:
        var_positivos=var_positivos+1
    elif var_número<0:
        var_negativos=var_negativos+1
    else:
        var_0=var_0+1
print(f"El número de positivos es {var_positivos}")
print(f"El número de negativos es {var_negativos}")
print(f"El número de ceros es {var_0}")