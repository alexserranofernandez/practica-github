#Inicio variables.
var_total=50
numero=1
#Con while aplicó condición.
while numero!=0 and var_total<=60:
    numero=int(input("Introduce un número:"))
#Aplicó condición para saber si es par o impar.
    if numero%2==0:
        var_total=var_total+numero
        print(var_total)
    if numero%2!=0:
        var_total=var_total-numero
        print(var_total)
    if numero==0:
        print("El número introducido es 0")
#Muestro resultado por pantalla.
print("Fin del programa")