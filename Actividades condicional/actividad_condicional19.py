#Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son 
#iguales
var1=int(input("Introduce un número"))
var2=int(input("Introduce otro número"))
if var1>var2:
    print(f"El número {var1} es mayor que el número {var2}.")
else:
    if var1<var2:
        print(f"El número {var2} es mayor que el número {var1}.")
    else:
        print(f"El número {var1} y número {var2} son iguales.")
