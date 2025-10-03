#Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos.
var1=float(input("Introduce la nota que has sacado"))
if var1>10 or var1<0:
    print("La nota que has introducido no está entre 0 y 10")
elif var1>=8.5:
    print(f"Has sacado un {var1} y es un excelente")
elif 8.5>var1 and var1>=6.5:
    print(f"Has sacado un {var1} y es un notable")
elif 6.5>var1 and var1>=5:
    print(f"Ha sacado un {var1} y es un satisfactorio")
elif var1<5:
    print(f"Has sacado un {var1} y es un suspenso")