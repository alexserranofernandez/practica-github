#Programa que al introducir una nota por teclado te diga si has aprobado o suspendido. 
#Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado.
var1=float(input("Introduce la nota que has sacado"))
if var1>10 or var1<0:
    print("La nota que has introducido no está entre 0 y 10")
else:
    if var1<5:    
        print(f"Has sacado un {var1} y has suspendido")
    else:
        print(f"Has sacado un {var1} y has aprobado")
