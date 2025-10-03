#Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un 
#notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota 
#introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos.
var1=float(input("Introduce la nota que has sacado"))
if var1>10 or var1<0:
    print("La nota que has introducido no está entre 0 y 10")
elif var1>=8.5:
    print(f"Has sacado un {var1} y es un excelente")
elif 8.5>var1>=6.5:
    print(f"Has sacado un {var1} y es un notable")
elif 6.5>var1>=5:
    print(f"Ha sacado un {var1} y es un satisfactorio")
elif var1<5:
    print(f"Has sacado un {var1} y es un suspenso")
