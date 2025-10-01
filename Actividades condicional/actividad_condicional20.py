#A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados 
#números entre 0 y 10
var1=int(input("Introduce un número del 1 al 10"))
var2=int(input("Introduce otro número del 1 al 10"))
if var1>10 or var2>10 or var1<0 or var2<0:
    print(f"Uno o los dos números están fuera de los límites establecidos")
else:
    if var1<var2:
        print(f"El número {var2} es mayor que el número {var1}")
    else:
        if var1>var2:
            print(f"El número {var1} es mayor que el número {var2}")
        else:
            print(f"El número {var1} y número {var2} son iguales")
