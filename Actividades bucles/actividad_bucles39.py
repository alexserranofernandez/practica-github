#Programa que pida n números y que, tras introducir el último número, debe aparecer por 
#pantalla el número total de positivos, negativos y número de 0.
var_repeticiones=int(input("Introduce el número de números que quieres introducir:"))
for i in range(var_repeticiones):
    var_número=int(input("Introduce un número:"))
    if var_número>0:
        p